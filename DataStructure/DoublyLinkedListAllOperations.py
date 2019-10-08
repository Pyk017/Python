class Node:
    def __init__(self,data):
        self.data = data
        self.next,self.prev = None,None

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
    choice = int(input("\nEnter Choice :- \n Press 1. to insert element in the Linked List.\n Press 2. to Print the Linked List items.\n Press 3. to Insert element in the LinkedList.\n Press 4. to delete a particular element from the LinkedList.\n Press 5. to reverse the Linked List.\n Press 6. to exit Immediately\n"))

    if choice is 1:
        while True:
            linklist.insert(input("Enter data :- "))
            ch = int(input("Enter 1 to continue or 0 to exit![1 / 0]?"))
            if ch is 0:
                break

    elif choice is 2:
        print ("Your Linked List is :- ")
        linklist.display()

    elif choice is 3:
        data = input("Enter the data you want to enter in the Linked List :- ")
        b = int(input('To perform Insert_After, Enter 0.\nTo perform Insert_Before: Enter 1.\n'))
        if b is 0:
            target = input("Enter the target element :- ")
            linklist.insert_After(data,target)
        elif b is 1:
            target = input("Enter the target element :- ")
            linklist.insert_Before(data,target)
        else:
            print ("Invalid Option!")

    elif choice is 4:
        target = input("Enter the target element that you want to delete :- ")
        linklist.deletion(target)

    elif choice is 5:
        linklist.reverse()
        print ("Your Reversed Linked List is :- ")
        linklist.display()

    elif choice is 6:
        break

    else:
        print("Invalid Input!")