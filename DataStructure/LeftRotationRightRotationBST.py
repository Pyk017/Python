class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BSTree:
    def __init__(self):
        self.root = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
        root.left.parent = root

    elif data > root.data:
        root.right = insert(root.right, data)
        root.right.parent = root

    return root


def print_level_order(root):
    if root is None:
        return None

    q = []
    p = root
    q.append(p)
    while len(q) > 0:
        print(q[0].data, end=" ")
        node = q.pop(0)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def get_height(root):
    return -1 if not root else max(1 + get_height(root.left), 1 + get_height(root.right))


def balance_factor(x):
    return get_height(x.left) - get_height(x.right)


def search(root, target):
    if root is None or root.data == target:
        return root

    elif root.data < target:
        return search(root.right, target)

    elif root.data > target:
        return search(root.left, target)


def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    y.parent = x.parent
    if tree.root is x:
        tree.root = y
    else:
        if x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

    x.parent = y


def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    x.parent = y.parent
    if y is tree.root:
        tree.root = x

    else :
        if y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

    y.parent = x


tree = BSTree()
print("Enter elements in the Tree.. \n Type no to stop the Process.")
while True:
    inp = input()
    if inp.lower() in 'no':
        break
    else:
        tree.root = insert(tree.root, int(inp))

print("Elements in the Tree are :- {}".format(tree.root.data))
print_level_order(tree.root)
while True:
    choice = input("\nEnter Left for Left Rotation and Right for right rotation and Press 0 to exit!\n").lower()
    target = int(input("\nEnter element which you want to rotate :- "))
    if choice in '0':
        break

    elif choice in 'left':
        node = search(tree.root, target)
        print(node.data)
        left_rotate(node)
        print_level_order(tree.root)

    elif choice in 'right':
        right_rotate(search(tree.root, target))
        print_level_order(tree.root)

    else:
        print("False Inputs !")

bal = int(input("Enter node to find the Balannce factor :- "))
print(balance_factor(search(tree.root, bal)))
