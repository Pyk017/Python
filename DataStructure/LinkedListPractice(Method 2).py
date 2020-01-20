class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
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
            self.lastNode = newNode

    def display(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.data,end =' ')
            currentNode = currentNode.next


listlist = LinkedList()
listlist.insert("Prakhar")
listlist.insert("Kumar")
listlist.insert("Kashyap")
listlist.insert(89)
listlist.insert(90)

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
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
            self.lastNode = newNode

    def display(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.data,end =' ')
            currentNode = currentNode.next


listlist = LinkedList()
listlist.insert("Prakhar")
listlist.insert("Kumar")
listlist.insert("Kashyap")
listlist.insert(89)
listlist.insert(90)

listlist.display()