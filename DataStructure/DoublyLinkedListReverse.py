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

    def reverse(self):
        pNode = self.head
        while pNode is not None:
            tempNode = pNode.prev
            pNode.prev = pNode.next
            pNode.next = tempNode
            pNode = pNode.prev

        if tempNode is not None:
            self.head = tempNode.prev

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
linklist.reverse()
print("\nLinked List after reversal is :- ")
linklist.display()
