class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            print("Stack UnderFlow!")
        else:
            pNode = self.top
            self.top = self.top.next
            del (pNode)

    def display(self):
        pNode = self.top
        while(pNode is not None):
            print (pNode.data, end=" ")
            pNode = pNode.next

    def peep(self):
        return self.top.data


stack = Stack()
while(True):
    choice = int(input("Enter choice : \n Press 1 to push element in the Stack.\n Press 2 to pop element from the Stack.\n Press 3 to peep the top element from the Stack.\n Press 4 to display the Whole Stack.\n Press 0 to exit Immediately."))
    if choice == 1:
        stack.push(int(input("\nEnter element to be Pushed into the Stack.")))
        print("Operation Completed!\n")

    elif choice == 2:
        stack.pop()
        print("\nOperation Completed!")

    elif choice == 3:
        print("Top element is : {} ".format(stack.peep()))

    elif choice == 4:
        print(stack.display())

    else:
        break
