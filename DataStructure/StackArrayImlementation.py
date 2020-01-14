<<<<<<< HEAD
def push(stack, target):
    stack.insert(0, target)

def pop(stack):
    stack.pop(0)

def peep():
    return stack[0]

def display(stack):
    return " ".join(map(str, stack[::-1]))


n = int(input("Enter Range :- "))
stack = [int(input("Enter {} element : ".format(i+1))) for i in range(n)]
while(True):
    choice = int(input("Enter choice : \n Press 1 to push element in the Stack.\n Press 2 to pop element from the Stack.\n Press 3 to peep the top element from the Stack.\n Press 4 to display the Whole Stack.\n Press 0 to exit Immediately."))
    if choice == 1:
        push(stack, int(input("\nEnter element to be Pushed into the Stack.")))
        print("Operation Completed!\n")

    elif choice == 2:
        pop(stack)
        print("\nOperation Completed!")

    elif choice == 3:
        print("Top element is : {} ".format(peep()))

    elif choice == 4:
        print(display(stack))

    else:
        break


=======
def push(stack, target):
    stack.insert(0, target)

def pop(stack):
    stack.pop(0)

def peep():
    return stack[0]

def display(stack):
    return " ".join(map(str, stack[::-1]))


n = int(input("Enter Range :- "))
stack = [int(input("Enter {} element : ".format(i+1))) for i in range(n)]
while(True):
    choice = int(input("Enter choice : \n Press 1 to push element in the Stack.\n Press 2 to pop element from the Stack.\n Press 3 to peep the top element from the Stack.\n Press 4 to display the Whole Stack.\n Press 0 to exit Immediately."))
    if choice == 1:
        push(stack, int(input("\nEnter element to be Pushed into the Stack.")))
        print("Operation Completed!\n")

    elif choice == 2:
        pop(stack)
        print("\nOperation Completed!")

    elif choice == 3:
        print("Top element is : {} ".format(peep()))

    elif choice == 4:
        print(display(stack))

    else:
        break


>>>>>>> Python repo committed
