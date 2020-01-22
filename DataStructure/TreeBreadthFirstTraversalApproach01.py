class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

def insert(root,data):
    if root is None :
        return Node(data)

    if data < root.data :
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

def printLevelOrder(root):
    for i in range(1, height(root) + 3):
        printGivenOrder(root, i)

def printGivenOrder(root, level):
    if root is None:
        return None
    if level is 1:
        print(root.data, end=" ")
    else:
        printGivenOrder(root.left, level - 1)
        printGivenOrder(root.right, level - 1)


def height(root):
    return -1 if root is None else max(1 + height(root.left), 1 + height(root.right))

tree = BSTree()
while True:
    ch = int(input("Enter choice :- \n Press 1 to enter element in the Tree. \n Press 2 to display the elements in the Tree.\n Press 3 to find the Height of the Tree.\n Press 0 to exit."))
    if ch is 1:
        while True:
            tree.root = insert(tree.root, int(input("Enter element :- ")))
            ch2 = int(input("Press 0 to exit or anything else to continue."))
            if ch2 == 0:
                break

    elif ch is 2:
        printLevelOrder(tree.root)
    elif ch is 3:
        print("Height of the Tree is :- {}".format(height(tree.root)))
    elif ch is 0:
        break
    else:
        print("Wrong Inputs!")

