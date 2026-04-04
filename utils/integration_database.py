def preparar_camada(camada, label_fonte):
    """
    Remove TODOS os campos exceto os essenciais e adiciona/atualiza a fonte_origem.
    Campos mantidos: 'fonte', 'cod_malha', 'cls_malha', 'fonte_origem'.
    """
    # 1. Definir a "Lista Branca" (campos que NÃO serão deletados)
    # Adicionamos 'fonte_origem' aqui para que, se ele já existir, não seja deletado
    whitelist = ['fonte', 'cod_malha', 'cls_malha']
    
    # 2. Identificar índices dos atributos que DEVEM ser excluídos
    all_fields = camada.fields()
    indices_para_excluir = []
    
    for i in range(all_fields.count()):
        field_name = all_fields[i].name()
        # Se o campo não estiver na whitelist, vai para a lista de exclusão
        if field_name not in whitelist:
            indices_para_excluir.append(i)
    
    # 3. Executar a exclusão em bloco (mais performático)
    camada.startEditing()
    if indices_para_excluir:
        camada.deleteAttributes(indices_para_excluir)
        camada.updateFields() # Atualiza a estrutura interna após deletar
           
    camada.commitChanges()
    
    print(f"   -> Limpeza concluída: Apenas campos essenciais mantidos em {label_fonte}.")

def filtrar_invalidos(input_path, output_path):
    """Extrai apenas geometrias válidas para evitar erros no Difference."""
    processing.run("native:extractbyexpression", {
        'INPUT': input_path,
        'EXPRESSION': 'is_valid($geometry)',
        'OUTPUT': output_path
    })

def remover_slivers(input_path, output_path, area_minima=5.0):
    """Remove polígonos menores que a área mínima (slivers)."""
    print(f"--> Filtrando polígonos espúrios (menores que {area_minima}m²)...")
    processing.run("native:extractbyexpression", {
        'INPUT': input_path,
        'EXPRESSION': f'$area > {area_minima}',
        'OUTPUT': output_path
    })

def processar_recorte_prioritario(lista_prioridade, output_folder, area_sliver=1.0):
    import os

    print("--- INICIANDO PROCESSAMENTO HIERÁRQUICO ---")
    
    if not os.path.exists(output_folder): os.makedirs(output_folder)
    temp_folder = os.path.join(output_folder, "temp_proc")
    if not os.path.exists(temp_folder): os.makedirs(temp_folder)

    camadas_finais_paths = []
    lista_mascaras_paths = []

    for i in range(len(lista_prioridade)):
        label = os.path.basename(lista_prioridade[i])[0:-4]
        print(f"\n[Camada {i+1}/{len(lista_prioridade)}] Lendo: {label}...")

        # 1. Configuração da Conexão com Filtro Especial
        lyr_raw = QgsVectorLayer(lista_prioridade[i], label, "ogr")

        if not lyr_raw.isValid():
            print(f"Erro ao carregar {label}. Pulando...")
            continue

        # 2. Preparar atributos e Rastreabilidade
        preparar_camada(lyr_raw, label)

        # 3. Corrigir Geometria Inicial em Disco
        path_fix = os.path.join(temp_folder, f"fix_{label}_v3c.gpkg")
        processing.run("native:fixgeometries", {'INPUT': lyr_raw, 'OUTPUT': path_fix})
        
        final_layer_path = os.path.join(output_folder, f"{i:02d}_{label}.gpkg")

        if i == 0:
            remover_slivers(path_fix, final_layer_path, area_sliver)
        else:
            # 4. Criar Máscara Acumulada
            raw_mask = os.path.join(temp_folder, f"raw_mask_{i}_v3c.gpkg")
            clean_mask = os.path.join(temp_folder, f"clean_mask_{i}_v3c.gpkg")
            
            processing.run("native:mergevectorlayers", {'LAYERS': lista_mascaras_paths, 'OUTPUT': raw_mask})
            filtrar_invalidos(raw_mask, clean_mask)
            
            # 5. Recorte (Difference)
            print(f"-> Aplicando recorte hierárquico...")
            path_diff = os.path.join(temp_folder, f"diff_{label}.gpkg")
            
            try:
                processing.run("native:difference", {
                    'INPUT': path_fix,
                    'OVERLAY': clean_mask,
                    'OUTPUT': path_diff
                })
            except:
                print(f"-> Falha no recorte direto. Tentando Buffer(0)...")
                path_b0 = os.path.join(temp_folder, f"b0_{label}_v3c.gpkg")
                processing.run("native:buffer", {'INPUT': path_fix, 'DISTANCE': 0, 'OUTPUT': path_b0})
                processing.run("native:difference", {'INPUT': path_b0, 'OVERLAY': clean_mask, 'OUTPUT': path_diff})
            
            # 6. Remoção de Slivers Pós-Recorte
            remover_slivers(path_diff, final_layer_path, area_sliver)

        camadas_finais_paths.append(final_layer_path)
        lista_mascaras_paths.append(final_layer_path)
        print(f"-> OK: {label} concluída.")

    # 7. Unificação Final
    print("\n--- GERANDO MALHA FINAL UNIFICADA ---")
    final_output = os.path.join(output_folder, "MALHA_FUNDIARIA_GO_CONSOLIDADA.shp")
    processing.run("native:mergevectorlayers", {
        'LAYERS': camadas_finais_paths,
        'OUTPUT': final_output
    })
    
    print(f"\nPROCESSO FINALIZADO!")
    print(f"Arquivo final: {final_output}")
    return final_output