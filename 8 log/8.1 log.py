from collections import deque
import random
import time

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

def bfs(adj_matrix, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        print(f"Посещаем вершину {vertex}")

        for adjacent, connected in enumerate(adj_matrix[vertex]):
            if connected and not visited[adjacent]:
                queue.append(adjacent)
                visited[adjacent] = True

#вероятность ребра #####################################
p = 0.4            #####################################

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

    start_vertex = int(input("Введите начальную вершину для обхода в ширину: "))

    visited = [False] * len(adjacency_matrix)
    
    ncomp = 0
    for i in range(graph_size):
        if not visited[i]:
            print("Новая компонента связности")
            ncomp += 1
            bfs(adjacency_matrix, i)
    print(ncomp," - компонент связности")




