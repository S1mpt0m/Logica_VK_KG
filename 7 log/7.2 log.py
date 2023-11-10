import random

def generate_random_adjacency_list(n, p):
    adjacency_list = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(i + 1, n):
            # Генерируем случайное число в диапазоне [0, 1]
            random_value = random.random()
            # Если случайное число меньше или равно p, то добавляем ребро
            if random_value <= p:
                adjacency_list[i].append(j)
                adjacency_list[j].append(i)

    return adjacency_list

def dfs(graph, visited, vertex):
    if not visited[vertex]:
        print("Посещаем вершину:", vertex)
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs(graph, visited, neighbor)

p = 0.5

while True:
    print("Введите -1 если хотите завершить программу ")
    n = int(input("Введите размер матрицы смежности: "))
    if n == -1:
        break
    
    # Генерируем список смежности
    adjacency_list = generate_random_adjacency_list(n, p)

    # Определяем размер графа
    edge_count = sum(len(neighbors) for neighbors in adjacency_list.values()) // 2

    # Определяем количество вершин
    graph_size = len(adjacency_list)

    # Выводим информацию о графе
    print("Список смежности:")
    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex}: {neighbors}")

    # Инициализация массива посещенных вершин
    visited = {vertex: False for vertex in range(graph_size)}

    # Начало обхода в глубину с первой вершины
    start_vertex = 0
    dfs(adjacency_list, visited, start_vertex)
