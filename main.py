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
#Funções customizadas
from utils import processing_raster as pr
from utils import integration_database as ia
from utils import integration_app as iap


# Configuração do Ambiente Standalone
qgis_prefix = r'Endereco do QGIS Desktop instalado'# i.e - C:\Program Files\QGIS 3.xx\apps\qgis'
QgsApplication.setPrefixPath(qgis_prefix, True)
qgs = QgsApplication([], False)
qgs.initQgis()

sys.path.append(r'C:\PROGRA~1\QGIS34~1.4\apps\qgis\python\plugins')

import processing
from processing.core.Processing import Processing
Processing.initialize() # <--- ESTA LINHA É A QUE RESOLVE O ERRO

# 4. Adicionar os algoritmos nativos
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())


# --- CONFIGURAÇÃO ---
ordem_prioridade = [
                    {'order':'1', 'src':'01_tih.shp'},
                    {'order':'2', 'src':'02_ucpi.shp'},
                    {'order':'3', 'src':'03_am.shp'},
                    {'order':'4', 'src':'04_incra_result_corrigido.shp'},
                    {'order':'5', 'src':'05_asse.shp'},
                    {'order':'6', 'src':'06_fnpd.shp'},
                    {'order':'7', 'src':'07_ucus.shp'},
                    {'order':'8', 'src':'08_glbp.shp'},
                    {'order':'9', 'src':'09_tqd.shp'},
                    {'order':'10', 'src':'10_tinh.shp'},
                    {'order':'11', 'src':'11_tqnd.shp'},
                    {'order':'13', 'src':'13_carss_v3.shp'},
                    {'order':'14', 'src':'14_carcs_v3.shp'}
]

ordem_prioridade_ia = [
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/hierarquia_vetor/mask/00_ma.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/hierarquia_vetor/mask/00_mancha_urbana.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_01_tih.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_02_ucpi.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_03_am.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_04_incra_result_corrigido.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_05_asse.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_06_fnpd.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_07_ucus.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_09_tqd.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_10_tinh.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_11_tqnd.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_13_carss_v3.shp',
                    'C:/Users/XXXX/Documents/Projetos/MalhaFundiaria/datasets/raster/expression_mask/selected_mask_14_carcs_v3.shp',
]
        
#Parâmetros de entrada e saida                                              
folder = input('Digite a pasta de entrada dos arquivos:')
outfolder = input('Digite a pasta de saida dos arquivos de máscara binária das malhas fundiárias:')
path_output_mask = input('Digite a pasta de saida dos arquivos de máscara binária das malhas fundiárias após hierarquia:')
folder_output_ia= input('Digite a pasta de saida dos arquivos da quantidade de sobreposição e mapa final hierarquizado (raster):')'
caminho_malha = input('Digite a saida do arquivo da malha fundiaria')
caminho_rl = input('Arquivo da reserva legal:')
fieldCodigoMalha = input('Digite o nome do atributo do códugo da malha')

#Processando as imagens
#Convertendo os vetores em imagens
pr.processRaster(folder,ordem_prioridade,outfolder)
time.sleep(20)

#Criando imagens de sobreposição de Hierarquização
pr.CalcStatistics(glob.glob(outfolder + '*.tif'),outfolder)
time.sleep(20)

#Selecionando as camadas
pr.selectedFeature(outfolder,folder,ordem_prioridade,path_output_mask)
time.sleep(20)

#Integração de malha fundiárias
ia.processar_recorte_prioritario(ordem_prioridade_ia, folder_output_ia)
time.sleep(20)

#Pre-processamento dos ativos
iap.integrar_apps_na_malha_completo(caminho_malha, caminho_apps, caminho_rl,folder_output_ia,fieldCodigoMalha)
time.sleep(20)

#Finalização Limpa
qgs.exitQgis()
