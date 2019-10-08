class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self,data):
        newNode = Node(data)
        if self.front is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def delete(self):
        if self.front is None:
            print("Stack UnderFlow!")
        else:
            pNode = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            del pNode

    def display(self):
        pNode = self.front
        while(pNode is not None):
            print (pNode.data, end=" ")
            pNode = pNode.next


queue = Queue()
while(True):
    choice = int(input(
        "Enter choice : \n Press 1 to Insert element in the Queue.\n Press 2 to delete element from the Queue.\n Press 3 to display the Queue.\n Press 0 to exit Immediately."))
    if choice == 1:
        queue.insert(int(input("\nEnter element to be Inserted in the Queue.")))
        print("Operation Completed!\n")

    elif choice == 2:
        queue.delete()
        print("\nOperation Completed!")

    elif choice == 3:
        print(queue.display())

    elif choice == 0:
        break

    else:
        print("Invalid Inputs.")