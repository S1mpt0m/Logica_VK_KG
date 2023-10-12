class Node:
    def __init__(self, inf):
        self.inf = inf  # полезная информация
        self.next = None  # ссылка на следующий элемент

head = None  # указатель на первый элемент очереди
tail = None  # указатель на последний элемент очереди
dlinna = 0  # переменная для хранения длины очереди

def get_struct():
    s = input("Введите название объекта: ")  # вводим данные
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

def dequeue():
    global head, dlinna
    if head is None:
        print("Очередь пуста")
        return
    removed = head
    head = head.next
    dlinna -= 1
    return removed.inf

def review():
    struc = head
    if head is None:
        print("Очередь пуста")
    while struc:
        print(f"Имя - {struc.inf}")
        struc = struc.next

loop = 0
gg = 0
while loop != 1:
    print("")
    print(" - - - - - - - - - - - - - - - ")
    print("")
    print("Выберите номер действия: ")
    print("Создать структуру - 1")
    print("Посмотреть список - 2")
    print("Удалить элемент - 3")
    print("Завершить программу - 4")
    gg = int(input())
    if gg == 1: # Создать структуру
        enqueue()
    if gg == 2: # Посмотреть список
        review()
    if gg == 3: # Удалить элемент
        dequeue()
    if gg == 4: # Выход из программы
        loop = 1

