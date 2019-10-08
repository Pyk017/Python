class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None
        self.pNode = None
        self.qNode = None

    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.lastNode = self.head

        else:
            self.lastNode.next = newNode
            self.lastNode = newNode

    def delete(self,target):
        self.pNode = self.head
        while self.pNode.data not in target and self.pNode is not None:
            self.qNode = self.pNode
            self.pNode = self.pNode.next

        if self.pNode is not None:
            if self.pNode is self.head:
                self.head = self.pNode.next
            else:
                self.qNode.next = self.pNode.next
            del self.pNode

        else:
            print ("Node Not Found!")


    def display(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.data)
            currentNode = currentNode.next

#Driver Code
linklist = LinkedList()
while True:
    linklist.insert(input("Enter data :- "))
    ch = int(input("Enter 1 to continue or 0 to exit![1 / 0]?"))
    if ch is 0:
        break

print ("Your Linked List is :- ")
linklist.display()

target = input("Enter target element to delete from the Linkedlist :- ")
linklist.delete(target)
print ("Your Linked List is :- ")
linklist.display()