#Importar módulos
from qgis.core import  QgsProject, QgsVectorLayer, QgsFeatureRequest, QgsFeature, QgsApplication,QgsDataSourceUri, QgsSpatialIndex,QgsGeometry,QgsField
from qgis import processing
import sys
from qgis.analysis import QgsNativeAlgorithms
import os
from PyQt5.QtCore import QVariant
import glob
import shutil
import time
import datetime

# Configuração do Ambiente Standalone
qgis_prefix = r'C:\Program Files\QGIS 3.xx\apps\qgis'
QgsApplication.setPrefixPath(qgis_prefix, True)
qgs = QgsApplication([], False)
qgs.initQgis()

sys.path.append(r'C:\PROGRA~1\QGIS34~1.4\apps\qgis\python\plugins')

import processing
from processing.core.Processing import Processing
Processing.initialize() # <--- ESTA LINHA É A QUE RESOLVE O ERRO

# 4. Adicionar os algoritmos nativos
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

def consolidar_malhas_qgis(output):
    """
    Utiliza o motor de processamento do QGIS para priorizar a malha SIGEF.
    """
    # 1. Carregar as camadas
    uri = QgsDataSourceUri()
    uri.setConnection("localhost", "5432", "postgis", "postgres", "123456")
    
    
    uri.setDataSource("public", "malha_fundiaria_imoveis_rurais_sigef", "geom")
    uri.setSql("uf_id = 52")
    layer_sigef = QgsVectorLayer(uri.uri(), "SIGEF_PostGIS", "postgres")
    
    uri.setDataSource("public", "malha_fundiaria_imoveis_rurais_snci", "geom")
    uri.setSql("uf_municip = 'GO'")
    layer_snci = QgsVectorLayer(uri.uri(), "SNCI_PostGIS", "postgres")
    
    
    print('Corrigindo a geometria SIGEF')
    fix_geo_sigef = processing.run("native:fixgeometries", {
        'INPUT': layer_sigef,
        'OUTPUT': 'memory:temp_fix_sigef'
    })['OUTPUT']
    
    print('Corrigindo a geometria SNCI')
    fix_geo_snci = processing.run("native:fixgeometries", {
        'INPUT': layer_snci,
        'OUTPUT': 'memory:temp_fix_snci'
    })['OUTPUT']
    
    if not layer_sigef.isValid() or not layer_snci.isValid():
        print("Erro ao carregar as camadas. Verifique os caminhos.")
        return

    print("Iniciando recorte da base SNCI...")

    # 2. Executar 'Difference': Remove do SNCI o que está sobreposto pelo SIGEF
    # Isso garante que não haverá duplicidade geométrica.
    params_diff = {
        'INPUT': fix_geo_snci,
        'OVERLAY': fix_geo_sigef,
        'OUTPUT': 'memory:SNCI_Recortado'
    }
    result_diff = processing.run("native:difference", params_diff)
    snci_recortado = result_diff['OUTPUT']

    print("Limpando resíduos topológicos (Slivers)...")
    
    # 3. Opcional: Filtrar polígonos irrelevantes gerados pelo recorte (ex: < 1m2)
    # No QGIS, isso pode ser feito via seleção por expressão
    snci_recortado.setSubsetString("area($geometry) > 5")

    print("Unificando camadas...")

    # 4. Mesclar as camadas: SIGEF (íntegro) + SNCI (apenas áreas não certificadas)
    outputFile = output
    params_merge = {
        'LAYERS': [layer_sigef, snci_recortado],
        'CRS': 'ESRI:102033',
        'OUTPUT': outputFile#'memory:Malha_Consolidada_Final'
    }
    result_final = processing.run("native:mergevectorlayers", params_merge)
    #result_final.setName("Malha_Consolidada_snci_sigef")
   
    print("Processo concluído. Camada 'Malha_Consolidada_Final' adicionada.")

def analisar_sobreposicao(layer,saida):
    """
    Input: Caminho completo para o .shp
    Output: Caminho completo para o novo .shp
    Lógica: Imóvel de menor área recorta o de maior área.
    """

    # 1. Carregar o Shapefile
    print(f"Lendo arquivo: {os.path.basename(layer)}")
    layer = QgsVectorLayer(layer, "camada_entrada", "ogr")

    features = [feat for feat in layer.getFeatures()]
    # 3. Ordenar por Área (Menor para Maior)
    print("Ordenando por área geométrica...")
    features_ordenadas = sorted(features, key=lambda f: f.geometry().area())

    # 4. Criar Índice Espacial para Performance
    print("Construindo índice espacial...")
    index = QgsSpatialIndex()
    for f in features_ordenadas:
        index.addFeature(f)

    # Mapeamento para busca rápida
    map_features = {f.id(): f for f in features_ordenadas}

    print("Iniciando recorte hierárquico otimizado...")
    
    # Lista para manter as geometrias que já "marcaram território"
    # Para performance, usamos uma lista de geometrias e verificamos apenas vizinhos
    geoms_processadas = [] 

    layer_resultado = QgsVectorLayer(f"Polygon?crs={layer.crs().authid()}", "resultado", "memory")
    layer_resultado.dataProvider().addAttributes(layer.fields())
    layer_resultado.updateFields()

    for i, feat in enumerate(features_ordenadas):
        geom_atual = feat.geometry()
        
        # Recortar a geometria atual contra tudo que já foi processado e que está perto
        for geom_fixa in geoms_processadas:
            if geom_atual.intersects(geom_fixa):
                geom_atual = geom_atual.difference(geom_fixa)
                if geom_atual.isEmpty():
                    break
        
        if not geom_atual.isEmpty() and geom_atual.area() > 1.0:
            feat.setGeometry(geom_atual)
            layer_resultado.dataProvider().addFeatures([feat])
            geoms_processadas.append(geom_atual)

        if i % 100 == 0:
            print(f"Processado: {i}/{len(features_ordenadas)} imóveis.")

    processing.run("native:savefeatures", {'INPUT': layer_resultado, 'OUTPUT': saida})
    print(f"Processamento concluído com sucesso.\nArquivos salvos em: {saida}")
   
# Exemplo de chamada (ajuste os caminhos para sua realidade):
srcIntegracao = 'C:/Users/Bernard/Documents/Projetos/MalhaFundiaria/datasets/tipos_malha_fundiaria/process_incra/mergerSNCI_SIGEF.shp'
srcIncraGeo = r'C:/Users/Bernard/Documents/Projetos/MalhaFundiaria/datasets/tipos_malha_fundiaria/04_incra_result_corrigido_v2.shp'

#Integração INCRA / SNCI
consolidar_malhas_qgis(srcIntegracao)

# Recorte social
analisar_sobreposicao(srcIntegracao,srcIncraGeo)

#Finalização Limpa
qgs.exitQgis()
