from collections import deque
import random

def generate_random_adjacency_matrix(n, p):
    adjacency_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            random_value = random.random()
            if random_value <= p:
                adjacency_matrix[i][j] = 1
                adjacency_matrix[j][i] = 1

    return adjacency_matrix

def generate_incidence_matrix(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    num_edges = sum(sum(row) for row in adjacency_matrix) // 2

    incidence_matrix = [[0] * num_edges for _ in range(num_vertices)]

    edge_index = 0

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if adjacency_matrix[i][j] == 1:
                incidence_matrix[i][edge_index] = 1
                incidence_matrix[j][edge_index] = 1
                edge_index += 1

    return incidence_matrix

def find_neighbors(incidence_matrix, current_vertex):
    num_vertices = len(incidence_matrix)
    neighbors = []

    for i in range(len(incidence_matrix[current_vertex])):
        if incidence_matrix[current_vertex][i] == 1:
            for j in range(num_vertices):
                if incidence_matrix[j][i] == 1 and j != current_vertex:
                    neighbors.append(j)

    return neighbors

def bfs(incidence_matrix, start):
    num_vertices = len(incidence_matrix)
    distances = [-1] * num_vertices

    queue = deque()
    queue.append(start)
    distances[start] = 0

    while queue:
        current_vertex = queue.popleft()

        neighbors = find_neighbors(incidence_matrix, current_vertex)

        for neighbor in neighbors:
            if distances[neighbor] == -1:
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
    
    incidence_matrix = generate_incidence_matrix(adjacency_matrix)

    print("Матрица смежности:")
    for row in adjacency_matrix:
        print(row)

    print("Матрица инцидентности:")
    for row in incidence_matrix:
        print(row)

    start_vertex = int(input("Введите стартовую вершину для поиска расстояний: "))

    distances = bfs(incidence_matrix, start_vertex)
    
    print(f"Расстояния от вершины {start_vertex}:")
    for vertex, distance in enumerate(distances):
        print(f"До вершины {vertex}: {distance}")

