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

def preorder_display(root):
    if root is not None:
        print(root.data, end=" ")
        preorder_display(root.left)
        preorder_display(root.right)

def inorder_display(root):
    if root is not None:
        inorder_display(root.left)
        print(root.data, end=" ")
        inorder_display(root.right)

def postorder_display(root):
    if root is not None:
        postorder_display(root.left)
        postorder_display(root.right)
        print(root.data, end=" ")

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
        while True:
            ch3 = int(input("\nEnter choice for Traversing the Tree. \n Press 1 for PreOrder Traversal. \n Press 2 for InOrder Traversal. \n Press 3 for PostOrder Traversal. \n Press 0 to exit.\n"))
            if ch3 == 1:
                preorder_display(tree.root)
            elif ch3 == 2:
                inorder_display(tree.root)
            elif ch3 == 3:
                postorder_display(tree.root)
            else:
                break
    elif ch is 3:
        print("Height of the Tree is :- {}".format(height(tree.root)))
    elif ch is 0:
        break

    else:
        print("Wrong Inputs!")

