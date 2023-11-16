import random

class Node:
    def __init__(self, inf):
        self.inf = inf  # полезная информация
        self.next = None  # ссылка на следующий элемент

head = None  # указатель на первый элемент очереди
tail = None  # указатель на последний элемент очереди
dlinna = 0  # переменная для хранения длины очереди

def get_struct():
    s = input("Введите начальную вершину для обхода в ширину: ")  # вводим данные
    if not s:
        print("Запись не была произведена")
        return None

    p = Node(s)
    p.next = None

    return p  # возвращаем экземпляр созданной структуры Node

def get_struct2(adjacent3):
    s = adjacent3  # вводим данные
    if not s:
        print("Запись не была произведена")
        return None

    p = Node(s)
    p.next = None

    return p  # возвращаем экземпляр созданной структуры Node

def enqueue():
    global head, tail, dlinna
    p = get_struct()
    if head is None and p is not None:  # если очереди нет, то устанавливаем голову и хвост очереди
        head = p
        tail = p
    elif head is not None and p is not None:  # добавляем элемент в конец очереди
        tail.next = p
        tail = p
    dlinna += 1  # увеличиваем длину очереди

def enqueue2(adjacent2):
    global head, tail, dlinna
    p = get_struct2(adjacent2)
    if head is None and p is not None:  # если очереди нет, то устанавливаем голову и хвост очереди
        head = p
        tail = p
    elif head is not None and p is not None:  # добавляем элемент в конец очереди
        tail.next = p
        tail = p
    dlinna += 1  # увеличиваем длину очереди
    
def dequeue():
    global head, dlinna
    if head is None:
        print("Очередь пуста")
        return
    removed = head
    head = head.next
    dlinna -= 1
    return removed.inf

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
    visited = [False] * len(adj_matrix)
    #Используем список как очередь
    enqueue()
    visited[start] = True

    while dlinna:
        vertex = int(head.inf)
        dequeue()  # Извлекаем элемент из начала очереди
        print(f"Посещаем вершину {vertex}")
        for adjacent, connected in enumerate(adj_matrix[vertex]):
            if connected and not visited[adjacent]:
                enqueue2(adjacent)  # Добавляем в конец очереди
                visited[adjacent] = True


# Параметры графа
p = 0.5

while True:
    print("Введите -1 если хотите завершить программу")
    n = int(input("Введите размер матрицы смежности: "))
    if n == -1:
        break
    
    # Генерируем матрицу смежности
    adjacency_matrix = generate_random_adjacency_matrix(n, p)
    
    # Вывод информации о графе
    print("Матрица смежности:")
    for row in adjacency_matrix:
        print(row)
    start_vertex = 0
    bfs(adjacency_matrix, start_vertex)
