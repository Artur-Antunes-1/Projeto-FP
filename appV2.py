from os import system
system('cls')

cont_treinos = 0
cont_competicoes = 0

def contagens():
    global cont_treinos, cont_competicoes
    
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
    
    opcao = int(input('Escolha a opção: '))
    if opcao == 1:
        adicionar()
    elif opcao == 2:
        visualizar()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        excluir()    
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
            
            data=(str(input("Data da atividade no formato DD MM AAAA: ")).split())
            datas="/".join(data)

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


def main():
    contagens()
    menu()

main()