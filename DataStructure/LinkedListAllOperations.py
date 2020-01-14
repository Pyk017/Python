<<<<<<< HEAD
class Node:
    def __init__(self,data):
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

    def insert_after(self,data,target):
        newNode = Node(data)
        pNode = self.head
        while pNode.data not in target and pNode is not None:
            pNode = pNode.next

        if pNode is not None:
            newNode.next = pNode.next
            pNode.next = newNode
        else:
            print ("Node not Found!")

    def insert_before(self,data,target):
        newNode = Node(data)
        pNode = self.head
        while pNode.data not in target and pNode is not None:
            self.lastNode = pNode
            pNode = pNode.next

        if pNode is not None:
            if pNode is self.head:
                newNode.next = pNode
                self.head = newNode
            else:
                newNode.next = pNode
                self.lastNode.next = newNode
        else:
            print ("Node not Found!")

    def delete(self,target):
        pNode = self.head
        while pNode.data not in target and pNode is not None:
            qNode = pNode
            pNode = pNode.next

        if pNode is not None:
            if pNode is self.head:
                self.head = pNode.next
            else:
                qNode.next = pNode.next
            del pNode
        else:
            print ("Node not Found!")

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def display(self):
        pNode = self.head
        while pNode is not None:
            print (pNode.data,end=" ")
            pNode = pNode.next
        print("\n")

linklist = LinkedList()
while True:
    choice = int(input("Enter Choice :- \n Press 1. to insert element in the Linked List.\n Press 2. to Print the Linked List items.\n Press 3. to Insert element in the LinkedList.\n Press 4. to delete a particular element from the LinkedList.\n Press 5. to reverse the Linked List.\n Press 6. to exit Immediately\n"))

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
            linklist.insert_after(data,target)
        elif b is 1:
            target = input("Enter the target element :- ")
            linklist.insert_before(data,target)
        else:
            print ("Invalid Option!")

    elif choice is 4:
        target = input("Enter the target element that you want to delete :- ")
        linklist.delete(target)

    elif choice is 5:
        linklist.reverse()
        print ("Your Reversed Linked List is :- ")
        linklist.display()

    elif choice is 6:
        break

    else:
        print("Invalid Input!")
=======
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.lastNode = self.head
        else:
            self.lastNode.next = newNode
            self.lastNode = newNode

    def insert_after(self, data, target):
        newNode = Node(data)
        pNode = self.head
        while pNode.data not in target and pNode is not None:
            pNode = pNode.next

        if pNode is not None:
            newNode.next = pNode.next
            pNode.next = newNode
        else:
            print ("Node not Found!")

    def insert_before(self, data, target):
        newNode = Node(data)
        pNode = self.head
        while pNode.data not in target and pNode is not None:
            self.lastNode = pNode
            pNode = pNode.next

        if pNode is not None:
            if pNode is self.head:
                newNode.next = pNode
                self.head = newNode
            else:
                newNode.next = pNode
                self.lastNode.next = newNode
        else:
            print("Node not Found!")

    def delete(self, target):
        pNode = self.head
        while pNode.data not in target and pNode is not None:
            qNode = pNode
            pNode = pNode.next

        if pNode is not None:
            if pNode is self.head:
                self.head = pNode.next
            else:
                qNode.next = pNode.next
            del pNode
        else:
            print("Node not Found!")

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def display(self):
        pNode = self.head
        while pNode is not None:
            print(pNode.data, end=" ")
            pNode = pNode.next
        print("\n")


linklist = LinkedList()
while True:
    choice = int(input("Enter Choice :- \n Press 1. to insert element in the Linked List.\n Press 2. to Print the "
                       "Linked List items.\n Press 3. to Insert element in the LinkedList.\n Press 4. to delete a "
                       "particular element from the LinkedList.\n Press 5. to reverse the Linked List.\n Press 6. to "
                       "exit Immediately\n"))

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
            linklist.insert_after(data, target)
        elif b is 1:
            target = input("Enter the target element :- ")
            linklist.insert_before(data, target)
        else:
            print ("Invalid Option!")

    elif choice is 4:
        target = input("Enter the target element that you want to delete :- ")
        linklist.delete(target)

    elif choice is 5:
        linklist.reverse()
        print ("Your Reversed Linked List is :- ")
        linklist.display()

    elif choice is 6:
        break

    else:
        print("Invalid Input!")
>>>>>>> Python repo committed
