class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree(root, r, data):
    if r is None:
        r = Node(data)
        if root is None:
            return r

        if data > root.data:
            root.left = r
        else:
            root.right = r

        return r

    if data == r.data:
        print("Элемент уже существует")
        return root
    else:
        if data > r.data:
            create_tree(r, r.left, data)
        else:
            create_tree(r, r.right, data)

    return root

def print_tree(r, l):
    if r is None:
        return

    print_tree(r.right, l + 1)
    for i in range(l):
        print(" ", end="")
    print(r.data)
    print_tree(r.left, l + 1)

root = None
start = 1

print("-1 - окончание построения дерева")
while start:
    D = int(input("Введите число: "))
    if D == -1:
        print("Построение дерева окончено\n")
        start = 0
    else:
        root = create_tree(root, root, D)

print_tree(root, 0)
