import random

def generate_random_adjacency_matrix(n, p):
    adjacency_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            # Генерируем случайное число в диапазоне [0, 1]
            random_value = random.random()
            # Если случайное число меньше или равно p, то устанавливаем ребро
            if random_value <= p:
                adjacency_matrix[i][j] = 1
                adjacency_matrix[j][i] = 1

    return adjacency_matrix

def dfs(graph, visited, vertex):

        print("Посещаем вершину:", vertex)
        visited[vertex] = True
        for neighbor in range(graph_size):
            if graph[vertex][neighbor] and not visited[neighbor]:
                dfs(graph, visited, neighbor)
    

#вероятность ребра #####################################
p = 0.5            #####################################

while True:
    print("Введите -1 если хотите завершить программу ")
    n = int(input("Введите размер матрицы смежности: "))
    if n == -1:
        break
    
    # Генерируем матрицу смежности
    adjacency_matrix = generate_random_adjacency_matrix(n, p)

    # Определяем размер графа
    edge_count = sum(sum(row) for row in adjacency_matrix) // 2

    # Определяем количество вершин
    graph_size = len(adjacency_matrix)

    # Выводим информацию о графе
    print("Матрица смежности:")
    for row in adjacency_matrix:
        print(row)

    # Инициализация массива посещенных вершин
    visited = [False] * graph_size

   # dfs(adjacency_matrix, visited, 1)

    ncomp = 0
    for i in range(graph_size):
        if not visited[i]:
            print("Новая компонента связности")
            ncomp += 1
            dfs(adjacency_matrix, visited, i)
    print(ncomp," - компонент связности")
