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
            if opcao in [1, 2, 3]:  # Adicionar data para as opções 1, 2 e 3
                metas_cont += 1
                file.write(f"Meta {metas_cont}:\n")
                if opcao == 1:
                    file.write("Tipo: Tempo\n")
                    tempo = float(input("Tempo em minutos: "))
                    file.write(f"Tempo: {tempo} min\n")
                elif opcao == 2:
                    file.write("Tipo: Distância\n")
                    distancia = float(input("Distância percorrida em Km: "))
                    file.write(f"Distância: {distancia} Km\n")
                elif opcao == 3:
                    file.write("Tipo: Tempo e Distância\n")
                    tempo = float(input("Tempo em minutos: "))
                    distancia = float(input("Distância percorrida em Km: "))
                    file.write(f"Tempo: {tempo} min\n")
                    file.write(f"Distância: {distancia} Km\n")
                
                # Adiciona o prazo para bater a meta
                prazo = input("Digite até quando deseja bater a meta (formato Dia/Mes/Ano): ")
                file.write(f"Prazo: {prazo}\n\n")
            
            elif opcao == 4:
                return metas()
            else:
                print("Entrada Inválida.")
                return adicionar_meta()

    except ValueError as ve:
        print(f"Erro de valor: {ve}. Por favor, insira valores válidos.")
    except Exception as e:
        print(f"Erro inesperado: {e}")