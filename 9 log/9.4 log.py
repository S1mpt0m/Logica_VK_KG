from collections import deque
import random

def generate_random_adjacency_list(n, p):
    adjacency_list = {i: [] for i in range(n)}
    
    for i in range(n):
        for j in range(i + 1, n):
            random_value = random.random()
            if random_value <= p:
                adjacency_list[i].append(j)
                adjacency_list[j].append(i)

    return adjacency_list

def dfs(adj_list, start):
    visited = [False] * len(adj_list)
    distances = [-1] * len(adj_list)

    def dfs_recursive(vertex, distance):
        visited[vertex] = True
        distances[vertex] = distance

        for neighbor in adj_list[vertex]:
            if not visited[neighbor]:
                dfs_recursive(neighbor, distance + 1)  # Увеличиваем расстояние на 1 при переходе к соседней вершине

    dfs_recursive(start, 0)
    return distances

p = 0.5

while True:
    print("Введите -1 если хотите завершить программу ")
    n = int(input("Введите размер графа (количество вершин): "))
    if n == -1:
        break
    
    adjacency_list = generate_random_adjacency_list(n, p)

    print("Списки смежности:")
    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex}: {neighbors}")

    start_vertex = int(input("Введите стартовую вершину для поиска расстояний: "))
    distances = dfs(adjacency_list, start_vertex)

    print(f"Расстояния DFS от вершины {start_vertex}:")
    for vertex, distance in enumerate(distances):
        print(f"До вершины {vertex}: {distance}")
