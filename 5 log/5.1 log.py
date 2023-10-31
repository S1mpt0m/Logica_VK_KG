import random

def generate_random_adjacency_matrix(n, p):
    adjacency_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # Генерируем случайное число в диапазоне [0, 1]
            random_value = random.random()
            # Если случайное число меньше или равно p, то устанавливаем ребро
            if random_value <= p:
                adjacency_matrix[i][j] = 1
            if i == j:
                adjacency_matrix[i][j] = 0


    return adjacency_matrix


#вероятность ребра #####################################
p = 0.5           #####################################

while True:
    print("Введите -1 если хотите завершить программу ")
    n = int(input("Введите размер матрицы смежности: "))
    if n == -1:
        break
    
    # Генерируем матрицу смежности
    adjacency_matrix = generate_random_adjacency_matrix(n, p)

    # Определяем размер графа
    summ = sum(sum(row) for row in adjacency_matrix)

    # Определяем размер графа (количество вершин)
    graph_size = len(adjacency_matrix)

    # Находим изолированные, концевые и доминирующие вершины
    isolated_vertices = [i for i in range(graph_size) if sum(adjacency_matrix[i]) == 0]
    end_vertices = [i for i in range(graph_size) if sum(adjacency_matrix[i]) == 1]
    dominating_vertices = []
    count = 0
    sum1 = 0
    for i in range(n):
        for j in range(n):
            sum1 += adjacency_matrix[i][j]
            sum1 += adjacency_matrix[j][i]
            sum1 -= adjacency_matrix[i][i]
        if sum1 == graph_size - 1:
            dominating_vertices.append(i)
            sum1 = 0


    # Выводим матрицу смежности, размер графа, количество рёбер и найденные вершины
    print("Матрица смежности:")
    for row in adjacency_matrix:
        print(row)

    print("Размер графа:", summ)
    print("Изолированные вершины:", isolated_vertices)
    print("Концевые вершины:", end_vertices)
    print("Доминирующие вершины:", dominating_vertices)


