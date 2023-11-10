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

def dfs_non_recursive(graph, start_vertex):
    stack = [start_vertex]
    visited = [False] * len(graph)

    while stack:
        vertex = stack.pop()
        print(vertex)
        if not visited[vertex]:
            print("Посещаем вершину:", vertex)
            visited[vertex] = True
            stack.append(neighbor for neighbor, has_edge in enumerate(graph[vertex]) if has_edge and not visited[neighbor])

p = 0.5

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

    # Начало не-рекурсивного обхода в глубину с первой вершины
    start_vertex = 0
    dfs_non_recursive(adjacency_matrix, start_vertex)
