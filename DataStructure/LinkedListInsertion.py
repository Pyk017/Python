<<<<<<< HEAD
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None
        self.currentNode = None
        self.nextNode = None

    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.lastNode = self.head

        else:
            self.lastNode.next = newNode
            self.lastNode = newNode

    def insert_after(self,data,target):
        self.currentNode = self.head
        while self.currentNode.data not in target and self.currentNode is not None:
            self.currentNode = self.currentNode.next

        if self.currentNode is not None:
            newNode = Node(data)
            newNode.next = self.currentNode.next
            self.currentNode.next = newNode
        else:
            print ('Node Not Found!')

    def insert_before(self,data,target):
        self.currentNode = self.head
        while self.currentNode.data not in target and self.currentNode is not None:
            self.nextNode = self.currentNode
            self.currentNode = self.currentNode.next

        if self.currentNode is not None:
            newNode = Node(data)
            if self.currentNode is self.head:
                newNode.next = self.head
                self.head = newNode
            else:
                newNode.next = self.currentNode
                self.nextNode.next = newNode
        else:
            print ('Node Not Found!')

    def display(self):
        self.currentNode = self.head
        while self.currentNode is not None:
            print(self.currentNode.data,end= ' ')
            self.currentNode = self.currentNode.next


linklist = LinkedList()
while True:
    linklist.insert(input("Enter data :- "))
    ch = int(input("Enter 1 to continue or 0 to exit![1 / 0]?"))
    if ch is 0:
        break

linklist.display()

val = input("Enter any data to enter :- ")
choice = int(input("Enter 1 to insertAfter or 0 to insertBefore."))
if choice is 1:
    target = input("Enter the target element from the linkedList.")
    linklist.insert_after(val,target)
elif choice is 0:
    target = input("Enter the target element from the linkedList.")
    linklist.insert_before(val, target)

=======
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None
        self.currentNode = None
        self.nextNode = None

    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.lastNode = self.head

        else:
            self.lastNode.next = newNode
            self.lastNode = newNode

    def insert_after(self,data,target):
        self.currentNode = self.head
        while self.currentNode.data not in target and self.currentNode is not None:
            self.currentNode = self.currentNode.next

        if self.currentNode is not None:
            newNode = Node(data)
            newNode.next = self.currentNode.next
            self.currentNode.next = newNode
        else:
            print ('Node Not Found!')

    def insert_before(self,data,target):
        self.currentNode = self.head
        while self.currentNode.data not in target and self.currentNode is not None:
            self.nextNode = self.currentNode
            self.currentNode = self.currentNode.next

        if self.currentNode is not None:
            newNode = Node(data)
            if self.currentNode is self.head:
                newNode.next = self.head
                self.head = newNode
            else:
                newNode.next = self.currentNode
                self.nextNode.next = newNode
        else:
            print ('Node Not Found!')

    def display(self):
        self.currentNode = self.head
        while self.currentNode is not None:
            print(self.currentNode.data,end= ' ')
            self.currentNode = self.currentNode.next


linklist = LinkedList()
while True:
    linklist.insert(input("Enter data :- "))
    ch = int(input("Enter 1 to continue or 0 to exit![1 / 0]?"))
    if ch is 0:
        break

linklist.display()

val = input("Enter any data to enter :- ")
choice = int(input("Enter 1 to insertAfter or 0 to insertBefore."))
if choice is 1:
    target = input("Enter the target element from the linkedList.")
    linklist.insert_after(val,target)
elif choice is 0:
    target = input("Enter the target element from the linkedList.")
    linklist.insert_before(val, target)

>>>>>>> Python repo committed
linklist.display()