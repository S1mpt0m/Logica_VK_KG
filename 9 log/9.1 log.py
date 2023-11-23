from collections import deque
import random
import time

def generate_random_adjacency_matrix(n, p):
    adjacency_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            random_value = random.random()
            if random_value <= p:
                adjacency_matrix[i][j] = 1
                adjacency_matrix[j][i] = 1

    return adjacency_matrix

def bfs(adj_matrix, start):
    distances = [-1] * len(adj_matrix)

    queue = deque()
    queue.append(start)
    distances[start] = 0

    while queue:
        current_vertex = queue.popleft()

        for neighbor, is_connected in enumerate(adj_matrix[current_vertex]):
            if is_connected and distances[neighbor] == -1:
                queue.append(neighbor)
                distances[neighbor] = distances[current_vertex] + 1

    return distances

p = 0.5

while True:
    print("Введите -1 если хотите завершить программу ")
    n = int(input("Введите размер матрицы смежности: "))
    if n == -1:
        break
    
    adjacency_matrix = generate_random_adjacency_matrix(n, p)

    print("Матрица смежности:")
    for row in adjacency_matrix:
        print(row)

    start_vertex = int(input("Введите стартовую вершину для поиска расстояний: "))

    start_time = time.time()
    distances = bfs(adjacency_matrix, start_vertex)
    end_time = time.time()

    print(f"Расстояния от вершины {start_vertex}:")
    for vertex, distance in enumerate(distances):
        print(f"До вершины {vertex}: {distance}")

    print(f"Время выполнения: {end_time - start_time} секунд")


