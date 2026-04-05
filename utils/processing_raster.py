#Importar módulos
from qgis import processing
import subprocess

# Configuração do Ambiente Standalone
qgis_prefix = r'C:\Program Files\QGIS 3.xx\apps\qgis'
gdal_prefix = r'C:\\Program Files\\QGIS 3.44.4\\bin\\'


def processRaster(folderIn,listData,folderOut):
       
    for i in listData:
        #Valor do pixel de cada Imagem
        valuepixel = i['order']

        #Endereço de cada arquivo
        lyr = i["src"] 
        lyrsrc = folderIn + lyr
        lyrout = folderOut + 'band_mf_'+ lyr[0:-4]+'.tif'

        #Endereco da ferramenta
        gdal_path = gdal_prefix + 'gdal_rasterize.exe'
        
        print(f'Convertendo a camada {lyr} ....')
        cmd = [
                   gdal_path,
                    '-burn', str(valuepixel),
                    '-tr', '10', '10',
                    '-co', 'COMPRESS=LZW',
                    '-a_nodata', '0',
                    '-ot', 'Byte',
                    lyrsrc,
                    lyrout
        ]
        #Executando o gdal_rasterize
        resultado = subprocess.run(cmd, capture_output=True, text=True)

        if resultado.returncode == 0:
            print("Rasterização concluída com sucesso! Salvo em:",lyrout)
        else:
            print(f"Erro: {resultado.stderr}")

def CalcStatistics(listRaster,output):

    #Parâmetros para o cálculo das estatísticas
    params = {
                        'INPUT': listRaster,
                        'STATISTIC': '',
                        'IGNORE_NODATA': True,
                        'CREATION_OPTIONS':'COMPRESS=LZW|PREDICTOR=2|ZLEVEL=9',
                        'OUTPUT_NODATA_VALUE':0,
                        'REFERENCE_LAYER': listRaster[3],
                        'OUTPUT': ''
    }
    metrics = {'overlap_count_layer':1,'landternure_layer':6}

    for keys in metrics:
        
        params['STATISTIC'] = metrics[keys]
        params['OUTPUT'] = output + keys + '.tif'

        print(f'Processando {keys}')
        processing.run("native:cellstatistics", params)
        
    print('Processo de hieraquização de camadas rasters finalizada...')


def selectedFeature(path_raster, path_vetor, ordem_prioridade, path_output):
    for w in ordem_prioridade:
        weight = w['order']
        mask_name = w['src'][0:-4]

        print(f"\n--- Processando: {mask_name} (Peso: {weight}) ---")
        
        # 1. Criar Máscara Binária
        params_calc = {
            'INPUT_A': path_raster + 'landternure_layer.tif',
            'BAND_A': 1,
            'FORMULA': f'(A == {int(weight)}) * 1', 
            'NO_DATA': 0,
            'RTYPE': 0,
            'OPTIONS': 'COMPRESS=LZW|PREDICTOR=2|ZLEVEL=9',
            'OUTPUT': path_output + 'Mask_' + mask_name + '.tif'
        }
        raster_result = processing.run("gdal:rastercalculator", params_calc)['OUTPUT']

        # 2. Corrigir Geometria
        fix_geo = processing.run("native:fixgeometries", {
            'INPUT': path_vetor + w['src'], 
            'OUTPUT': 'memory:'
        })['OUTPUT']

        # 3. Estatística Zonal (Feature Based)
        # IMPORTANTE: Usamos 'COLUMN_PREFIX': 'st_' e pedimos a média [2]
        params_zonal = {
            'INPUT': fix_geo,
            'INPUT_RASTER': raster_result,
            'RASTER_BAND': 1,
            'COLUMN_PREFIX': 'st_',
            'STATISTICS': [2], # Mean
            'OUTPUT': 'memory:'
        }
        zonal_layer = processing.run("native:zonalstatisticsfb", params_zonal)['OUTPUT']

        # 4. Filtrar resultados
        # DICA: Verificamos se a feição tem o valor médio e se ele é maior que o limiar
        # O uso de COALESCE trata casos onde st_mean é NULL (áreas sem sobreposição)
        expressao = 'coalesce("st_mean", 0) >= 0.1'
        
        output_file = path_output + 'selected_mask_' + w['src']
        
        params_filter = {
            'INPUT': zonal_layer,
            'EXPRESSION': expressao,
            'OUTPUT': output_file
        }
        
        try:
            processing.run("native:extractbyexpression", params_filter)
            print(f'Sucesso! Salvo em: {output_file}')
        except Exception as e:
            print(f'Erro ao filtrar a camada {mask_name}: {e}')

        # Limpeza de memória
        del fix_geo
        del zonal_layer    

