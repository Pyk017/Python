class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None
        self.currentNode = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
            self.lastNode = self.head
        else:
            self.lastNode.next = newNode
            self.lastNode = newNode

    def display(self):
        self.currentNode = self.head
        while self.currentNode is not None:
            print(self.currentNode.data)
            self.currentNode = self.currentNode.next

while True:
    choice = int(input("Enter Choice :- \n Press 1. to insert element in the Linked List.\n Press 2 to Print the Linked List items.\n Press 3. to exit Immediately.\n"))
    linklist = LinkedList()
    if choice is 1:
        while True:
            node = Node(input("Enter data :- "))
            linklist.insert(node)
            ch = input("Enter Yes to continue or No to exit![y / n]?")
            if ch in 'n':
                break
    elif choice is 2:
        print ("Your Linked List is :- ")
        linklist.display()
    elif choice is 3:
        break
    else:
        print("Invalid Input!")

