from collections import deque
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

def convert_to_adjacency_list(adj_matrix):
    adj_list = {}
    for i, row in enumerate(adj_matrix):
        adj_list[i] = [j for j, val in enumerate(row) if val == 1]
    return adj_list

def bfs(adj_list, start):
    visited = [False] * len(adj_list)
    queue = deque([start])
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        print(f"Посещаем вершину {vertex}")

        for adjacent in adj_list[vertex]:
            if not visited[adjacent]:
                queue.append(adjacent)
                visited[adjacent] = True
                
#вероятность ребра #####################################
p = 0.5            #####################################

while True:
    print("Введите -1 если хотите завершить программу ")
    n = int(input("Введите размер матрицы смежности: "))
    if n == -1:
        break
    
    # Генерируем матрицу смежности
    adjacency_matrix = generate_random_adjacency_matrix(n, p)
    
    # Получаем список смежности из матрицы смежности
    adjacency_list = convert_to_adjacency_list(adjacency_matrix)

    # Определяем размер графа
    edge_count = sum(sum(row) for row in adjacency_matrix) // 2

    # Определяем количество вершин
    graph_size = len(adjacency_matrix)

    # Выводим список смежности
    print("Список смежности:")
    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex}: {neighbors}")

    start_vertex = int(input("Введите начальную вершину для обхода в ширину: "))
    bfs(adjacency_list, start_vertex)
