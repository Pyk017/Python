<<<<<<< HEAD
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True :
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def print(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.data)
            currentNode = currentNode.next


fnode = Node("Prakhar")
snode = Node("Kumar")
thnode = Node("Kashyap")
link = LinkedList()
link.insert(fnode)
link.insert(snode)
link.insert(thnode)
=======
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True :
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def print(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.data)
            currentNode = currentNode.next


fnode = Node("Prakhar")
snode = Node("Kumar")
thnode = Node("Kashyap")
link = LinkedList()
link.insert(fnode)
link.insert(snode)
link.insert(thnode)
>>>>>>> Python repo committed
link.print()