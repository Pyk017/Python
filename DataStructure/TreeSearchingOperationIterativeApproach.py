class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            p = self.root
            while True:
                if data < p.data:
                    if p.left:
                        p = p.left
                    else:
                        p.left = Node(data)

                elif data > p.data:
                    if p.right:
                        p = p.right
                    else:
                        p.right = Node(data)

                else:
                    break

    def search(self,target):
        p = self.root
        while p.data != target and p is not None:

            if target > p.data:
                p = p.right

            elif target < p.data:
                p = p.left

        if p.data == target:
            print ("Element found in the Tree!\n")
        else:
            print ("Element doesnot Found!\n")

def printLevelOrder(root):
    if root is None:
        return None
    else:
        q = []
        q.append(root)
        while len(q) > 0:

            print(q[0].data, end=" ")
            node = q.pop(0)

            if node.left :
                q.append(node.left)

            if node.right :
                q.append(node.right)

def height(root):
    return -1 if root is None else min(1 + height(root.left), 1 + height(root.right))

tree = BSTree()
while True:
    ch = int(input("Enter choice :- \n Press 1 to enter element in the Tree. \n Press 2 to display the elements in the Tree.\n Press 3 to find the Height of the Tree. \n Press 4 to search an element in the Tree. \n Press 0 to exit."))
    if ch is 1:
        while True:
            tree.insert(int(input("Enter element :- ")))
            ch2 = int(input("Press 0 to exit or anything else to continue."))
            if ch2 == 0:
                break

    elif ch is 2:
        printLevelOrder(tree.root)

    elif ch is 3:
        print("Height of the Tree is :- {}".format(height(tree.root)))

    elif ch is 4:
        target = int(input("\nEnter a target element :- "))
        tree.search(target)

    elif ch is 0:
        break

    else:
        print("Wrong Inputs!")
