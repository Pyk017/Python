<<<<<<< HEAD
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

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

    def deletion(self,target):
        pNode = self.head
        while pNode.data not in target and pNode is not None:
            pNode = pNode.next

        if pNode.data in target:

            if pNode.next is not None and pNode.prev is not None:
                pNode.next.prev = pNode.prev
                pNode.prev.next = pNode.next

            elif pNode.prev is None:
                pNode.next.prev = None

            else:
                pNode.prev.next = None
        else:
            print ("Node not Found!")

    def display(self):
        pNode = self.head
        while pNode is not None:
            print (pNode.data,end = " ")
            pNode = pNode.next

linklist = DLinkedList()
while True:
    linklist.insert(input("Enter data :- "))
    ch = int(input("Enter 1 to continue or 0 to exit![1 / 0]?"))
    if ch is 0:
        break

linklist.display()
target = input("Enter target element to Delete from the list.")
linklist.deletion(target)
=======
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

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

    def deletion(self,target):
        pNode = self.head
        while pNode.data not in target and pNode is not None:
            pNode = pNode.next

        if pNode.data in target:

            if pNode.next is not None and pNode.prev is not None:
                pNode.next.prev = pNode.prev
                pNode.prev.next = pNode.next

            elif pNode.prev is None:
                pNode.next.prev = None

            else:
                pNode.prev.next = None
        else:
            print ("Node not Found!")

    def display(self):
        pNode = self.head
        while pNode is not None:
            print (pNode.data,end = " ")
            pNode = pNode.next

linklist = DLinkedList()
while True:
    linklist.insert(input("Enter data :- "))
    ch = int(input("Enter 1 to continue or 0 to exit![1 / 0]?"))
    if ch is 0:
        break

linklist.display()
target = input("Enter target element to Delete from the list.")
linklist.deletion(target)
>>>>>>> Python repo committed
linklist.display()