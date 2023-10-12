class Node:
    def __init__(self, inf):
        self.inf = inf  # полезная информация
        self.next = None  # ссылка на следующий элемент

head = None  # указатель на первый элемент списка
last = None  # указатель на последний элемент списка
f = None  # другой указатель (например, для операций)
dlinna = 0  # переменная для хранения длины списка
top = None  # указатель на вершину стека
dlinna = 0  # переменная для хранения размера стека

def get_struct():
    s = input("Введите название объекта: ")  # вводим данные
    if not s:
        print("Запись не была произведена")
        return None

    p = Node(s)
    p.next = None

    return p  # возвращаем экземпляр созданной структуры Node


def review():
    struc = top
    if top is None:
        print("Стек пуст")
    while struc:
        print(f"Имя - {struc.inf}")
        struc = struc.next

def push():
    global top, dlinna
    p = get_struct()
    if p is not None:
        p.next = top  # новый элемент указывает на текущую вершину стека
        top = p  # обновляем вершину стека
        dlinna += 1  # увеличиваем размер стека

def pop():
    global top, dlinna
    if top is None:
        print("Стек пуст")
        return None
    removed = top
    top = top.next  # обновляем вершину стека
    dlinna -= 1  # уменьшаем размер стека
    return removed.inf

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
        push()
    if gg == 2: # Посмотреть список
        review()
    if gg == 3: # Удалить элемент
        pop()
    if gg == 4: # Выход из программы
        loop = 1
