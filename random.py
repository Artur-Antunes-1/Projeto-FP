treinos_disponiveis = {"Corrida Leve de 5 km", "Treino de Velocidade 3 km", "Ladeira 2 km", "Longão de 10 km", "Intervalado 5x400m"}
treinos_ja_sugeridos = set()

def sugestao_de_treino():
    global treinos_disponiveis, treinos_ja_sugeridos

    if not treinos_disponiveis:
        treinos_disponiveis = treinos_ja_sugeridos
        treinos_ja_sugeridos = set()

    sugestao = treinos_disponiveis.pop()
    treinos_ja_sugeridos.add(sugestao)
    
    print(f"Sugestão de treino: {sugestao}")