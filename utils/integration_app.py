#Importar módulos
from qgis import processing

def integrar_apps_na_malha_completo(path_malha, path_apps, path_rl, path_output,campo_id_imovel):
    from qgis.core import  QgsProject, QgsVectorLayer, QgsFeatureRequest, QgsFeature, QgsApplication,QgsDataSourceUri, QgsSpatialIndex,QgsGeometry,QgsField
    print("Iniciando processamento integrado com APP...")
    
    # Carregar camadas
    lyr_malha = QgsVectorLayer(path_malha, "Malha", "ogr")
    lyr_apps = QgsVectorLayer(path_apps, "APPs", "ogr")
    lyr_rl = QgsVectorLayer(path_rl, "RL", "ogr")
    
    if not lyr_malha.isValid() or not lyr_apps.isValid() or not lyr_rl.isValid():
        print("Erro: Verifique os caminhos dos arquivos.")
        return

    # 1. Corrigir Geometrias
    print("Passo 1: Corrigindo geometrias...")
    fix_geo_malha = processing.run("native:fixgeometries", {'INPUT': lyr_malha, 'OUTPUT': 'TEMPORARY_OUTPUT'})['OUTPUT']
    fix_geo_app = processing.run("native:fixgeometries", {'INPUT': lyr_apps, 'OUTPUT': 'TEMPORARY_OUTPUT'})['OUTPUT']
    fix_geo_rl = processing.run("native:fixgeometries", {'INPUT': lyr_rl, 'OUTPUT': 'TEMPORARY_OUTPUT'})['OUTPUT']

    # 2. Prioridade APP: Remover áreas de APP de dentro da Reserva Legal
    print("Passo 2: Recortando APP da Reserva Legal (Prioridade APP)...")
    # Trocando 'memory:' por 'TEMPORARY_OUTPUT' para usar o disco se necessário
    processing.run("native:difference", {
        'INPUT': fix_geo_rl,
        'OVERLAY': fix_geo_app,
        'OUTPUT': path_output +  '/temp_proc/rl_com_clear.gpkg'
    })['OUTPUT']

    # Interseção RL com Malha (Ajustado: fix_malha -> fix_geo_malha)
    processing.run("native:intersection", {
        'INPUT': path_output +  '/temp_proc/rl_com_clear.gpkg',
        'OVERLAY': fix_geo_malha,
        'OUTPUT':  path_output +  '/temp_proc/rl_com_id.gpkg'#'TEMPORARY_OUTPUT'
    })['OUTPUT']

    
    print("Passo 3: Vinculando dados da Malha às APPs e RL...")
    # Interseção APP com Malha
    processing.run("native:intersection", {
        'INPUT': fix_geo_app,
        'OVERLAY': fix_geo_malha, 
        'OUTPUT': path_output +  '/temp_proc/app_com_id.gpkg'#'TEMPORARY_OUTPUT'
    })['OUTPUT']
    
   
    print(f"--- SUCESSO ---")

