<<<<<<< HEAD
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

def check_binary_tree (root):
    return check(root, -1, 1000)

def check (node, min, max):
    if not (min < node.data < max):
        return False
    if node.left:
        if not (node.left, min, node.data):
            return False

    if node.right:
        if not(node.right, node.data, max):
            return False

    return True

tree = BSTree()
inputs = list(map(int, input("Enter elements in the Tree :- ").split(' ')))
for i in inputs:
    tree.root = insert(tree.root, i)

print ("Element in the Tree are :- ",printLevelOrder(tree.root))
=======
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

def check_binary_tree (root):
    return check(root, -1, 1000)

def check (node, min, max):
    if not (min < node.data < max):
        return False
    if node.left:
        if not (node.left, min, node.data):
            return False

    if node.right:
        if not(node.right, node.data, max):
            return False

    return True

tree = BSTree()
inputs = list(map(int, input("Enter elements in the Tree :- ").split(' ')))
for i in inputs:
    tree.root = insert(tree.root, i)

print ("Element in the Tree are :- ",printLevelOrder(tree.root))
>>>>>>> Python repo committed
print ("It is a Binary Tree.") if check_binary_tree(tree.root) else print ("It is not a Binary Tree.")