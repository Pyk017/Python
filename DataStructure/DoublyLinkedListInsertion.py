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

    def insert_After(self,data,target):
        newNode = Node(data)
        pNode = self.head
        while pNode.data not in target and pNode is not None:
            pNode = pNode.next

        if pNode is not None:
            newNode.prev = pNode
            newNode.next = pNode.next
            if pNode.next is not None:
                pNode.next.prev = newNode
            pNode.next = newNode
        else:
            print ("Node not Found!")

    def insert_Before(self,data,target):
        newNode = Node(data)
        self.lastNode = self.head
        while self.lastNode.data not in target and self.lastNode is not None:
            self.lastNode = self.lastNode.next

        if self.lastNode is not None:
            if self.lastNode is self.head:
                self.lastNode.prev = newNode
                newNode.next = self.lastNode
                self.head = newNode
            else:
                newNode.next = self.lastNode
                newNode.prev = self.lastNode.prev
                self.lastNode.prev.next = newNode
                self.lastNode.prev = newNode
        else:
            print ("Node not Found!")

    def display(self):
        pNode = self.head
        while pNode is not None:
            print (pNode.data,end=" ")
            pNode = pNode.next



linklist = DLinkedList()
while True:
    linklist.insert(input("Enter data :- "))
    ch = int(input("Enter 1 to continue or 0 to exit![1 / 0]?"))
    if ch is 0:
        break

linklist.display()
val = input("Enter any data to enter :- ")
while True:
    choice = int(input("Enter 1 to insertAfter or 2 to insertBefore 3 to display the List. Or 0 to exit!"))
    if choice is 1:
        target = input("Enter the target element from the linkedList.")
        linklist.insert_After(val,target)
    elif choice is 2:
        target = input("Enter the target element from the linkedList.")
        linklist.insert_Before(val,target)
    elif choice is 3:
        linklist.display()
    #ch = int(input("Enter 1 to continue or 0 to exit![1 / 0]?"))
    elif choice is 0:
        break
    else:
        print ("Wrong Input!!")






