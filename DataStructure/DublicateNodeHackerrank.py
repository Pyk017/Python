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
            print(currentNode.data)
            currentNode = currentNode.next

def dublicate(head):
    p = head
    q = head.next
    while p is not None and q is not None:
        if p.data == q.data:
            p.next = q.next
            q = q.next
        else:
            p = q
            q = q.next

    return head


#Driver Code
linklist = LinkedList()
while True:
    linklist.insert(input("Enter data :- "))
    ch = int(input("Enter 1 to continue or 0 to exit![1 / 0]?"))
    if ch is 0:
        break

print ("Your Linked List is :- ")
linklist.display()
print(linklist.head.data)
llist = dublicate(linklist.head)
linklist.head = llist
print(linklist.display())
# print ("Reverse of the LinkedList is :- ")
# linklist.reverse()