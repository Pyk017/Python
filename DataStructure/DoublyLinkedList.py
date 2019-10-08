class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.lastNode = self.head
        else:
            self.lastNode.next = newNode
            newNode.prev = self.lastNode
            self.lastNode = newNode

    def display(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.data,end=" ")
            currentNode = currentNode.next

linklist = DLinkedList()
ch = 9
while ch is not 0:
    data = input("Enter data in the Linked list :- ")
    linklist.insert(data)
    ch = int(input("Enter choice :- \n Press 1 to continue.\n Press 0 to exit Immediately!"))

print ("Your Linked List is :- ")
linklist.display()

