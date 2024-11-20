from os import system, name
from datetime import datetime
import random
from time import sleep
system("cls" if name == "nt" else "clear")

cont_treinos = 0
cont_competicoes = 0
metas_cont = 0

def contagens():
    global cont_treinos, cont_competicoes, metas_cont
    try:
        with open('metas.txt', 'r', encoding="utf-8") as file:
            conteudo_metas = file.readlines()
            for linha in conteudo_metas:
                if linha.startswith("Meta "):
                    metas_cont += 1
    except FileNotFoundError:
        pass  # Se o arquivo não existir, mantém a contagem de metas em 0
    except Exception as e:
        print(f"Erro inesperado ao carregar contagens de metas: {e}")
    
    try:
        with open('dados.txt', 'r', encoding="utf-8") as file:
            conteudo = file.readlines()
            for linha in conteudo:
                if linha.startswith("ID: C"):  # Checa se a linha é uma competição
                    cont_competicoes += 1
                elif linha.startswith("ID: T"):  # Checa se a linha é um treino
                    cont_treinos += 1
    except FileNotFoundError:
        pass  # Se o arquivo não existir, mantém as contagens em 0
    except Exception as e:
        print(f"Erro inesperado ao carregar contagens: {e}")
    try:
        with open('dados.txt', 'r', encoding="utf-8") as file:
            conteudo = file.readlines()
            for linha in conteudo:
                if linha.startswith("ID: C"):  # Checa se a linha é uma competição
                    cont_competicoes += 1
                elif linha.startswith("ID: T"):  # Checa se a linha é um treino
                    cont_treinos += 1
    except FileNotFoundError:
        pass  # Se o arquivo não existir, mantém as contagens em 0
    except Exception as e:
        print(f"Erro inesperado ao carregar contagens: {e}")

def menu():
    print("\033[1;32m", 6*'-' + "MENU" + 6*'-', "\033[m")
    print('\033[1;34m[ 1 ] Adicionar')
    print('[ 2 ] Visualizar')
    print('[ 3 ] Atualizar')
    print('\033[1;31m[ 4 ] Excluir\033[m')
    print('\033[1;33m[ 5 ] Metas\033[m')
    print("\033[1;33m[ 6 ] Sugestão\033[m")
    print('\033[1;33m[ 7 ] Filtragem de treinos\033[m')
    print("\033[1;33m[ 8 ] Pace\033[m")
    print('[ 0 ] Sair')
    
    opcao = int(input('Escolha a opção: '))
    if opcao == 1:
        adicionar()
    elif opcao == 2:
        visualizar()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        excluir()   
    elif opcao == 5:
        metas()
    elif opcao == 6:
        aleatorio()
    elif opcao == 7:
        filtragem()
    elif opcao == 8: 
        pace()
    elif opcao == 0:
        print('Saindo...')
        exit()
    else:
        print('Entrada Inválida:')
        return menu()

def excluir():
    try:
        with open('dados.txt', 'r', encoding="utf-8") as file:
            conteudo = file.readlines()
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return
   
    if not conteudo:  # Se o arquivo estiver vazio, print
        print("Não há treinos ou competições registrados para excluir.")
        print()
        menu()

    id = input("ID do treino ou competição a ser excluído: ").title()
    found = False
    
    global cont_treinos, cont_competicoes
    if id.startswith("C"):  # Se o ID for uma competição
        cont_competicoes -= 1
    elif id.startswith("T"):  # Se o ID for um treino
        cont_treinos -= 1
    
    if not id.startswith("C") and not id.startswith("T"):  # Se o ID não começar com "C" ou "T", print
        print("ID inválido. Por favor, insira um ID válido.")
        return excluir()
    

    
    for i in range(len(conteudo)):
        if id in conteudo[i]:
            print(f"Treino/Competição {id} encontrado na linha {i + 1}")
            found = True

            del conteudo[i:i + 7]  # Deleta a linha com o ID e as 7 linhas seguintes (detalhes do treino/competição)
            conteudo = [linha for linha in conteudo if linha.strip()]

            try:
                with open('dados.txt', 'w', encoding="utf-8") as file:
                    file.writelines(conteudo)
                print(f"Treino/Competição {id} excluído com sucesso!")
                print()
            except Exception as e:
                print(f"Erro inesperado ao excluir: {e}")
            return menu()
    
    if not conteudo:  # Se o arquivo estiver vazio, print
        print("Nenhum treino/competição registrado.")
        print()
        return menu()
    
    if not found:
        print(f"Treino/Competição {id} não encontrado.")
        print()
        menu()

def adicionar():
    tipo = input("\nSalvar como:\n[ c ] Competição ou [ t ] Treino: ").lower().strip()
    
    try:
        with open('dados.txt', 'a+', encoding="utf-8") as file:  # Abre o arquivo para leitura e escrita
            if tipo == "c":
                global cont_competicoes
                cont_competicoes += 1
                file.write(f"ID: C{cont_competicoes}\n")
                id = f"C{cont_competicoes}"
                file.write("Competição:\n")
                print(f"Competição de id: {id} adicionada com sucesso!")

            elif tipo == "t":
                global cont_treinos
                cont_treinos += 1
                file.write(f"ID: T{cont_treinos}\n")
                id = f"T{cont_treinos}"
                file.write("Treino:\n")
                print(f"Treino de id: {id} adicionada com sucesso!")

            else:
                print('Entrada Inválida:')
                return adicionar()
            
             # Valida a data
            while True:
                try:
                    data = input("Data da atividade no formato DD MM AAAA: ")
                    dia, mes, ano = map(int, data.split())
                    data_valida = datetime(ano, mes, dia)  # Tenta criar uma data
                    datas = data_valida.strftime("%d/%m/%Y")  # Formata a data para o formato desejado
                    break  # Sai do loop se a data for válida
                except ValueError:
                    print("Data inválida. Por favor, insira uma data existente no formato DD MM AAAA.")
            
            file.write(f"Data: {datas}\n")

            distancia = float(input("Distância percorrida em Km: "))    
            file.write(f"Distância: {distancia}Km\n")

            tempo = float(input("Tempo em minutos: "))
            file.write(f"Tempo: {tempo} min\n")

            local = input("Localização da atividade: ").title()
            file.write(f"Localização: {local}\n")

            clima = input("Condições climáticas durante a atividade: ").title()
            file.write(f"Clima: {clima}\n\n")

    except ValueError as ve:
        print(f"Erro de valor: {ve}. Por favor, insira valores válidos.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    print()
    menu()

def visualizar():
    try:
        with open('dados.txt', 'r', encoding="utf-8") as file:
            conteudo = file.readlines()
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return

    if not conteudo:  # Se o arquivo estiver vazio, print
        print("Nenhum treino/competição registrado.")
        print()
        return menu()
    
    print(f"Competições registradas: {cont_competicoes}")
    print(f"Treinos registrados: {cont_treinos}")
    print("Escolha a opção de visualização:\n[ 1 ] Todos os treinos/competições\n[ 2 ] Treino/Competição específico\n[ 3 ] Voltar\n")

    opcao = int(input())
    
    if opcao == 1:
        print("Treinos/Competições registrados:\n")
        for linha in conteudo:
            print(linha.strip())  
        sleep(3)    

    elif opcao == 2:
        id = input("ID do treino ou competição a ser visualizado: ").strip().title()  # Strip whitespace
        found = False
        
        for i in range(len(conteudo)):
            if id in conteudo[i]:  # Checa se o ID é encontrado na linha
                print(f"Treino/Competição {id} encontrado na linha {i + 1}")
                print("Treino/Competição específico:\n")
                print(conteudo[i])  # Print da linha com o ID
                treino_especifico = conteudo[i + 1:i + 7]  # Captura as 6 linhas seguintes (detalhes do treino/competição)
                
                for linha in treino_especifico:
                    print(linha.strip())  # Remove espaços em branco
                print()
                found = True  # Marca a id como encontrada
                break  # Sai do loop após encontrar a id
        sleep(3) 

        if not found:  # Print apenas se o ID não foi encontrado
            print(f"Treino/Competição {id} não encontrado.")
    elif opcao == 3:
        return menu()
    else:
        print('Entrada Inválida:')
        return visualizar()

    menu()

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
            # Garante que existem 6 linhas seguintes para ler os detalhes do treino/competição
            if i + 6 >= len(conteudo):  # Se não há 6 linhas seguintes, não é possível atualizar
                print("Informações insuficientes para atualizar.")
                print("Verificando a quantidade de linhas disponíveis.")
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
                
            except IndexError:
                print()
                print("Bug encontrado: por favor insira novamente")
                return atualizar()
            except ValueError as ve:
                print(f"Erro de valor: {ve}. Por favor, verifique a entrada.")
                return

            # Mostra as opções de atualização
            opcao = int(input("Escolha a opção de atualização:\n[ 1 ] Atualizar data\n[ 2 ] Atualizar distância\n[ 3 ] Atualizar tempo\n[ 4 ] Atualizar localização\n[ 5 ] Atualizar clima\n[ 6 ] Voltar\n"))
            if opcao == 1:
                data = input("Nova data no formato DD MM AAAA: ")
                dados_atuais['data'] = data
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

            # Atualiza os dados com novos valores
            conteudo[i] = conteudo[i]  # Mantém o id inalterado
            conteudo[i + 1] = f"Tipo: {dados_atuais['tipo']}\n"
            conteudo[i + 2] = f"Data: {dados_atuais['data']}\n"
            conteudo[i + 3] = f"Distância: {dados_atuais['distancia']}Km\n"
            conteudo[i + 4] = f"Tempo: {dados_atuais['tempo']} min\n"
            conteudo[i + 5] = f"Localização: {dados_atuais['local']}\n"
            conteudo[i + 6] = f"Clima: {dados_atuais['clima']}\n"

            # Escreve as novas informações no arquivo
            try:
                with open('dados.txt', 'w', encoding="utf-8") as file:
                    file.writelines(conteudo)
                print(f"Treino/Competição {id} atualizado com sucesso!")
                return menu()
            except Exception as e:
                print(f"Erro inesperado ao salvar a atualização: {e}")
            return # Sai da função após atualizar o treino/competição
        
            
    if not found:  # Se o ID não foi encontrado, print
        print(f"Treino/Competição {id} não encontrado.")
        menu()

def metas():
    print()
    print("[ 1 ] Adicionar meta:")
    print("[ 2 ] Visualizar meta(s):")
    print("[ 3 ] Excluir meta:")
    print("[ 4 ] Voltar")
    print()
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        adicionar_meta()
    elif opcao == 2:
        visualizar_meta()
    elif opcao == 3:
        excluir_meta()
    elif opcao == 4:
        return menu()
    else:
        print("Entrada Inválida:")
        return metas()

def adicionar_meta():
    try:
        with open('metas.txt', 'a+', encoding="utf-8") as file:  # Abre o arquivo para leitura e escrita
            print("[ 1 ] Adicionar meta de tempo:")
            print("[ 2 ] Adicionar meta de distância:")
            print("[ 3 ] Adicionar meta de tempo e distância:")
            print("[ 4 ] Voltar")
            print()
            global metas_cont
            opcao = int(input("Escolha a opção: "))
            if opcao == 1:
                metas_cont += 1
                file.write(f"Meta {metas_cont}:\n") 
                file.write("Tipo: Tempo\n")
                tempo = float(input("Tempo em minutos: "))
                file.write(f"Tempo: {tempo} min\n\n\n")
            elif opcao == 2:
                metas_cont += 1
                file.write(f"Meta {metas_cont}:\n") 
                file.write("Tipo: Distância\n")
                distancia = float(input("Distância percorrida em Km: "))
                file.write(f"Distância: {distancia}Km\n\n\n")
            elif opcao == 3:
                metas_cont += 1
                file.write(f"Meta {metas_cont}:\n") 
                file.write("Tipo: Tempo e Distância\n")
                tempo = float(input("Tempo em minutos: "))
                distancia = float(input("Distância percorrida em Km: "))
                file.write(f"Tempo: {tempo} min\n")
                file.write(f"Distância: {distancia}Km\n\n")
            elif opcao == 4:
                return metas()
            else:
                print("Entrada Inválida:")
                return adicionar_meta()
            
             # Adiciona o prazo para bater a meta
            prazo = input("Digite até quando deseja bater a meta (formato Dia/Mes/Ano): ")
            try:
                prazo_data = datetime.strptime(prazo, "%d/%m/%Y")
                hoje = datetime.now()
                if prazo_data <= hoje:
                    raise ValueError("A data deve ser futura.")
                dias_restantes = (prazo_data - hoje).days
                file.write(f"Prazo: {prazo} (Faltam {dias_restantes} dias)\n\n")
                print(f"Meta adicionada! Faltam {dias_restantes} dias para alcançar o prazo.")
            except ValueError as ve:
                print(f"Erro: {ve}. Por favor, insira uma data válida e futura.")
                return adicionar_meta()

    except ValueError as ve:
        print(f"Erro de valor: {ve}. Por favor, insira valores válidos.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    print()
    metas()

def visualizar_meta():
    try:
        with open('metas.txt', 'r', encoding="utf-8") as file:
            conteudo_metas = file.readlines()
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return
    if not conteudo_metas:  # Se o arquivo estiver vazio, print
        print("Nenhuma meta registrada.")
        print()
        return metas()
    
    print("Metas registradas:\n")
    for linha in conteudo_metas:
        print(linha.strip())  
    print()
    sleep(2)    
    return metas()

def excluir_meta():
    try:
        with open('metas.txt', 'r', encoding='utf-8') as file:
            conteudo_metas = file.readlines()

        # Coletar todas as metas registradas
        metas_registradas = []
        for i in range(len(conteudo_metas)):
            if conteudo_metas[i].startswith("Meta"):
                # Começa a coletar as linhas da meta
                meta = {}
                meta['linhas'] = [conteudo_metas[i].strip()]  # Inclui a primeira linha da meta
                # Coleta as linhas subsequentes até a próxima meta ou o final do arquivo
                j = 1  # Começa a contar a partir da segunda linha
                while i + j < len(conteudo_metas) and not conteudo_metas[i + j].startswith("Meta"):
                    meta['linhas'].append(conteudo_metas[i + j].strip())
                    j += 1
                metas_registradas.append(meta)
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return

    if not metas_registradas:  # Se o arquivo estiver vazio, print
        print("Nenhuma meta registrada.")
        print()
        return metas()

    print("Metas registradas:\n")
    for idx, meta in enumerate(metas_registradas):
        print(f"Meta de ID [ {idx + 1} ]: {meta['linhas'][0][0:6]}")  # Mostra o ID da meta  
    print()
    
    try:
        id = int(input("ID da meta a ser excluída: "))
        if id < 1 or id > len(metas_registradas):
            print("ID inválido.")
            return metas()

        # Calcula o número de linhas a serem excluídas
        lines_to_delete = len(metas_registradas[id - 1]['linhas'])
        # Encontrar a posição da meta no arquivo
        meta_index = conteudo_metas.index(metas_registradas[id - 1]['linhas'][0] + '\n')
        
        # Remove as linhas da meta do arquivo
        del conteudo_metas[meta_index:meta_index + lines_to_delete]

    except ValueError:
        print("Erro: ID da meta não encontrado.")
        return metas()
    except Exception as e:
        print(f"Erro inesperado ao excluir a meta: {e}")
        return metas()

    try:
        with open('metas.txt', 'w', encoding='utf-8') as file:
            file.writelines(conteudo_metas)
        print(f"Meta {id} excluída com sucesso!")
        return metas()
    except Exception as e:
        print(f"Erro inesperado ao salvar a modificação: {e}")
        return metas()

def pace():
    try:
        with open('dados.txt', 'r', encoding="utf-8") as file:
            conteudo = file.readlines()
    except FileNotFoundError:
        print("Nenhum treino ou competição registrado para calcular o pace.")
        return
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return

    print("\nPace:")
    for i in range(len(conteudo)):
        if conteudo[i].startswith("ID: "):  
            id_atividade = conteudo[i].strip()
            tipo = "Treino" if "T" in id_atividade else "Competição"
            distancia = 0
            tempo = 0
            
            for j in range(i + 1, len(conteudo)):
                if conteudo[j].startswith("Distância:"):
                    distancia = float(conteudo[j].split(":")[1].replace("Km", "").strip())
                elif conteudo[j].startswith("Tempo:"):
                    tempo = float(conteudo[j].split(":")[1].replace("min", "").strip())
                elif conteudo[j].startswith("ID:"):  
                    break
            
            if distancia > 0 and tempo > 0:
                pace = tempo / distancia
                minutos = int(pace)
                segundos = int((pace - minutos) * 60)
                print(f"{id_atividade} ({tipo}) - Pace: {minutos}min {segundos:02d}s/km")
            else:
                print(f"{id_atividade} ({tipo}) - Dados insuficientes para calcular o pace.")
    print()

def aleatorio():
    treinos_fixos = [
    "Corrida de 5km com ritmo moderado",
    "Treino intervalado de 10 x 400m",
    "Corrida de 8km com inclinação leve",
    "Corrida de 3km com ritmo acelerado",
    "Treino de subida - 6 x 200m em subida",
    "Corrida de recuperação de 5km em ritmo leve",
    "Treino longo de 15km em ritmo confortável",
    "Corrida de 2km em velocidade máxima",
    "Treino intervalado de 5 x 800m",
    "Corrida de 10km em ritmo progressivo"
]
    try:
        
        if not treinos_fixos:
            raise ValueError("Não é possível selecionar um treino")
        
        treino = random.choice(treinos_fixos)
        print()
        print("Sugestão de treino:", treino)
        print()
        sleep(3)    
        return menu()
    except ValueError as ve:
        print(f"Erro: {ve}")
        menu()
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        menu()

def filtragem():
    try:
        with open('dados.txt','r',encoding='utf-8') as file:
            arquivo=file.readlines()
    except FileNotFoundError:
            return 'Arquivo não encontrado. '

    if not arquivo:
        print('Não foi registrado nenhum treino/competição') 
        menu()

    print()
    print('[ 1 ] Para filtrar  treinos por tempo.')
    print('[ 2 ] Para filtrar treinos por distância.')
    print('[ 3 ] Voltar.')
    print()
    opcao=int(input('Digite sua opção: '))
    if opcao==1:
        try:
            filtrar_tempo=float(input('Você deseja filtrar os treinos por qual tempo? (Em minutos):  '))
        except ValueError:
            print('Digite o valor em números.')
            return filtragem()
        tempo_existe=False
        for i in range(len(arquivo)):
            if arquivo[i].startswith('Tempo: '):
                tempo=float(arquivo[i].split(': ')[1].replace('min','').strip())
                if tempo==filtrar_tempo:
                    if not tempo_existe:
                        print(f'\nTreinos realizados em {filtrar_tempo} minutos\n')
                        tempo_existe=True
                    print((''.join(arquivo[i-4:i+3]).strip()))
        if tempo_existe:
            input('\nAperte ENTER para voltar para o menu de filtragem.')
            filtragem()
        else:
            print('Digite o tempo de treinos que você já tenha realizado.')
            filtragem()

    
    if opcao==2:
        try:
            filtrar_distancia=float(input('Você deseja filtrar os treinos por qual distância? (Em km): '))                
        except ValueError:
            print('Digite o valor em números')
            return filtragem()
        distancia_existe=False
        for i in range(len(arquivo)):
            if arquivo[i].startswith('Distância: '):
                distancia=float(arquivo[i].split(':')[1].replace('Km','').strip())
                if distancia==filtrar_distancia:
                    if not distancia_existe:
                        print(f'\nTreinos realizados de {filtrar_distancia} km.')
                        distancia_existe=True
                    print((''.join(arquivo[i-3:i+4]).strip()))
        if distancia_existe:
            input('\nAperte ENTER para voltar ao menu de filtragem.')
            filtragem()
        else: 
            print('Digite uma distância de treinos que você já realizou.')   
            filtragem()         
    if opcao == 3:
        menu()

def extra():
    cont = 0
    try:
        with open("musicas.txt", "r+", encoding="UTF-8")as file:
            conteudo = file.readlines()
            while True:
            
                print("digite [1] para recomendações de musicas para seu treino")
                print("digite [2] para musicas aleatorias para seu treino")
                print("digite [3] para escrever as proximas recomendações de musicas para seu treino")
            
                resposta = int(input("digite a resposta: "))     
                
                if resposta == 1:
                    cont+=1
                    print(conteudo[cont])

                
                elif resposta == 2:
                    musica_aleatoria = random.choice(conteudo)    
                    print(musica_aleatoria)
                
                elif resposta == 3:
                    print("Escreva a musica para recomendar ")
                    recomendar = input('Escreva de forma ("musica" - "cantor/banda") \n =>')
                    file.write(recomendar)
                
                else:
                    print("Responda [1]-[2]-[3]")
                    continue

    except FileNotFoundError:
        print("Arquivo não encontrado")
    except ValueError:
        print("Use apenas numeros para essa resposta")

extra()


def main():
    contagens()
    menu()

main()