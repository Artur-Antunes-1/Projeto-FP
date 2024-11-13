from datetime import datetime

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