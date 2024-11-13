from datetime import datetime

def atualizar():
    try:
        with open('dados.txt', 'r', encoding="utf-8") as file:
            conteudo = file.readlines()  # Lê todas as linhas do arquivo na memória
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return

    if not conteudo:  # Se o arquivo estiver vazio, print
        print("Nenhum treino/competição registrado.")
        print()
        return menu()

    id = input("ID do treino ou competição a ser atualizado: ").strip().title()  
    found = False  # Para rastrear se o ID foi encontrado
    
    for i in range(len(conteudo)):
        if id in conteudo[i]:  # Checa se o ID é encontrado na linha
            print(f"Treino/Competição {id} encontrado na linha {i + 1}")
            found = True
            if i + 6 >= len(conteudo):  # Se não há 6 linhas seguintes, não é possível atualizar
                print("Informações insuficientes para atualizar.")
                return

            try:              
                dados_atuais = {
                    'tipo': conteudo[i + 1].strip(),
                    'data': conteudo[i + 2].split(": ")[1].strip(),
                    'distancia': float(conteudo[i + 3].split(": ")[1].replace("Km", "").strip()),
                    'tempo': float(conteudo[i + 4].split(": ")[1].replace("min", "").strip()),
                    'local': conteudo[i + 5].split(": ")[1].strip(),
                    'clima': conteudo[i + 6].split(": ")[1].strip()
                }
                
            except (IndexError, ValueError) as e:
                print(f"Erro ao processar os dados existentes: {e}")
                return

            opcao = int(input("Escolha a opção de atualização:\n[ 1 ] Atualizar data\n[ 2 ] Atualizar distância\n[ 3 ] Atualizar tempo\n[ 4 ] Atualizar localização\n[ 5 ] Atualizar clima\n[ 6 ] Voltar\n"))
            if opcao == 1:
                # Validação da nova data
                while True:
                    try:
                        data = input("Nova data no formato DD MM AAAA: ")
                        dia, mes, ano = map(int, data.split())
                        data_valida = datetime(ano, mes, dia)  # Verifica se a data é válida
                        dados_atuais['data'] = data_valida.strftime("%d/%m/%Y")
                        break
                    except ValueError:
                        print("Data inválida. Por favor, insira uma data existente no formato DD MM AAAA.")
                        
            elif opcao == 2:
                distancia = float(input("Nova distância percorrida em Km: "))
                dados_atuais['distancia'] = distancia
            elif opcao == 3:
                tempo = float(input("Novo tempo em minutos: "))
                dados_atuais['tempo'] = tempo
            elif opcao == 4:
                local = input("Nova localização da atividade: ").title()
                dados_atuais['local'] = local
            elif opcao == 5:
                clima = input("Novas condições climáticas durante a atividade: ").title()
                dados_atuais['clima'] = clima
            elif opcao == 6:
                return menu()
            else:
                print('Entrada Inválida:')
                return atualizar()

            # Atualiza o conteúdo com os novos valores
            conteudo[i] = conteudo[i]  # Mantém o id inalterado
            conteudo[i + 1] = f"Tipo: {dados_atuais['tipo']}\n"
            conteudo[i + 2] = f"Data: {dados_atuais['data']}\n"
            conteudo[i + 3] = f"Distância: {dados_atuais['distancia']}Km\n"
            conteudo[i + 4] = f"Tempo: {dados_atuais['tempo']} min\n"
            conteudo[i + 5] = f"Localização: {dados_atuais['local']}\n"
            conteudo[i + 6] = f"Clima: {dados_atuais['clima']}\n"

            try:
                with open('dados.txt', 'w', encoding="utf-8") as file:
                    file.writelines(conteudo)
                print(f"Treino/Competição {id} atualizado com sucesso!")
                return menu()
            except Exception as e:
                print(f"Erro inesperado ao salvar a atualização: {e}")
            return 
        
    if not found:  # Se o ID não foi encontrado
        print(f"Treino/Competição {id} não encontrado.")
        menu()