class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BSTree:
    root = None
    def insert(self, data):
        if BSTree.root is None:
            BSTree.root = Node(data)

        else :
            temp = Node(data)
            pNode = BSTree.root
            q = None
            while pNode is not None:
                q = pNode
                if pNode.data > data:
                    pNode = pNode.left
                else:
                    pNode = pNode.right

            if q.data > data:
                q.left = temp
                temp.parent = q

            else:
                q.right = temp
                temp.parent = q

        return BSTree.root


def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.data, end=' ')
        printInOrder(root.right)

def printPostOrder(root):
    if root is not None:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.data, end=' ')

def printPreOrder(root):
    if root is not None:
        print(root.data, end=' ')
        printPreOrder(root.left)
        printPreOrder(root.right)

def printLevelOrder(root):
    if root is None:
        return None

    else:
        p = root
        q = []
        q.append(p)
        while (len(q) > 0):

            print (q[0].data, end=" ")
            node = q.pop(0)

            if node.left:
                q.append(node.left)

            if node.right :
                q.append(node.right)


def height(root):
    return -1 if root is None else max(1 + height(root.left), 1 + height(root.right))

def search(root,data):
    if root is None:
        return root
    elif data < root.data:
        return search(root.left, data)
    elif data > root.data:
        return search(root.right, data)
    else:
        return root

def minValue(node):
    if node.left:
        node = node.left

    return node

def successor(root, data):
    root = search(root, data)
    if root.right :
        return minValue(root.right)

    else:
        p = root.parent
        while p is not None and root == p.right:
            root = p
            p = p.parent

        return p

def delete(root, data):
    x = search(root, data)
    if x:
        if x.left and x.right:
            if x is x.parent.left:
                x.parent.left = None
            else:
                x.parent.right = None

        elif x.left is not None and x.right is None:
            if x is x.parent.left:
                x.parent.left = x.left
            else:
                x.parent.right = x.left

        elif x.left is None and x.right is not None:
            if x is x.parent.left:
                x.parent.left = x.right
            else:
                x.parent.right = x.right

        else:
            y = successor(root, x.data)
            x.data = y.data
            return delete(root, y.data)

        return True

    else:
        return False



tree = BSTree()
while True:
    ch = int(input("Enter choice :- \n Press 1 to enter element in the Tree. \n Press 2 to display the elements in the Tree.\n Press 3 to find the Height of the Tree. \n Press 4 to search an element in the Tree. \n Press 5 to find the Successor of any element.\n Press 6 to delete any element from the Tree.\n Press 0 to exit."))
    if ch is 1:
        while True:
            BSTree.root = tree.insert(int(input("Enter element :- ")))
            ch2 = int(input("Press 0 to exit or anything else to continue."))
            if ch2 == 0:
                break

    elif ch is 2:
        while True:
            ch3 = int(input("\nEnter choice for Traversing the Tree. \n Press 1 for PreOrder Traversal. \n Press 2 for InOrder Traversal. \n Press 3 for PostOrder Traversal. \n Press 0 to exit.\n"))
            if ch3 == 1:
                printPreOrder(BSTree.root)
            elif ch3 == 2:
                printInOrder(BSTree.root)
            elif ch3 == 3:
                printPostOrder(BSTree.root)
            elif ch3 == 4:
                printLevelOrder(BSTree.root)
            else:
                break

    elif ch is 3:
        print("Height of the Tree is :- {}".format(height(tree.root)))

    elif ch is 4:
        target = int(input("\nEnter a target element :- "))
        newNode = search(tree.root, target)
        print("Element found in the Tree!") if newNode.data is target else print("Element not Found in the Tree.")

    elif ch is 5:
        node = successor(BSTree.root, int(input("\nEnter element :- ")))
        print ("Successor of your element is :- {}".format(node.data))

    elif ch is 6:
        msg = delete(BSTree.root, int(input("Enter  element to delete from the Tree :- ")))
        print("\nDeletion Successful!\n") if msg else print ("\n No element present for Deletion. \n")

    elif ch is 0:
        break

    else:
        print("Wrong Inputs!")
