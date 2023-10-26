class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None
count = 0

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

    if data > r.data:
        create_tree(r, r.left, data)
    else:
        create_tree(r, r.right, data)

    return root

def print_tree(r, l):
    if r is None:
        return

    print_tree(r.right, l + 1)
    print(" - " * l, r.data)
    print_tree(r.left, l + 1)

def find(r, D_find):
    global count

    if r is None:
        return count

    if r.data == D_find:
        count += 1

    find(r.right, D_find)
    find(r.left, D_find)

def obxod(r):

    
    if r.right is not None:
        obxod(r.right)
    print(r.data)
    if r.left is not None:
        obxod(r.left)
    

root = None
print("-1 - окончание построения дерева")
while True:
    D = int(input("Введите число: "))
    if D == -1:
        print("Построение дерева окончено\n")
        break
    else:
        root = create_tree(root, root, D)

print_tree(root, 0)

obxod(root)
