class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

class BSTree:
    def __init__(self):
        self.root = None

def insert(root, data):
    if (root is None):
        return Node(data)
    else:
        if data > root.data:
            root.right = insert(root.right, data)
        elif data < root.data:
            root.left = insert(root.left, data)

    return root

def printLevelOrder(root):
    if root is None:
        return None

    q = []
    l = []
    p = root
    q.append(p)
    while len(q) > 0 :
        l.append(q[0].data)
        node = q.pop(0)
        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

    return l

def get_lowest_common_ancestor(root, a, b):
    if root.data > a and root.data > b :
        root = get_lowest_common_ancestor(root.right, a, b)
    elif root.data < a and root.data < b:
        root = get_lowest_common_ancestor(root.left, a, b)

    return root

tree = BSTree()
inputs = list(map(int, input("Enter elements in the Tree :- ").split(' ')))
for i in inputs:
    tree.root = insert(tree.root, i)
a, b = list(map(int, input("Enter two elements from the Tree :- ").split(" ")))
print ("Lowest Common Ancestor between your numbers is :- ",get_lowest_common_ancestor(tree.root, a, b).data)