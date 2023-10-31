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

#вероятность ребра #####################################
p = 0.6            #####################################

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

    # Находим изолированные, концевые и доминирующие вершины
    isolated_vertices = [i for i in range(graph_size) if sum(adjacency_matrix[i]) == 0]                                                 
    end_vertices = [i for i in range(graph_size) if sum(adjacency_matrix[i]) == 1]                                                      
    dominating_vertices = [i for i in range(graph_size) if sum(adjacency_matrix[i]) > 0 and sum(adjacency_matrix[i]) == graph_size - 1]

    # Строим матрицу инцидентности
    incidence_matrix = generate_incidence_matrix(adjacency_matrix)

    # Определяем количество рёбер на основе матрицы инцидентности
    num_edges_from_incidence = len(incidence_matrix[0])

    # Выводим информацию о графе, включая количество рёбер из матрицы инцидентности
    print("Матрица смежности:")
    for row in adjacency_matrix:
        print(row)
        
    # Выводим также матрицу инцидентности
    print("Матрица инцидентности:")
    for row in incidence_matrix:
        print(row)

    print("Размер графа (из матрицы смежности):", edge_count)
    print("Изолированные вершины (из матрицы смежности) :", isolated_vertices)
    print("Концевые вершины (из матрицы смежности) :", end_vertices)
    print("Доминирующие вершины (из матрицы смежности) :", dominating_vertices)
    print("Размер графа (из матрицы инцидентности):", num_edges_from_incidence)




