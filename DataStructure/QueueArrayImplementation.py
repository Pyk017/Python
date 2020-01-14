<<<<<<< HEAD
def insert(queue, target):
    queue.append(target)

def delete(queue):
    queue.pop(0)

def display(queue):
    print(' '.join(map(str, queue)))


n = int(input("Enter Range :- "))
queue = [int(input("Enter {} element : ".format(i+1))) for i in range(n)]
while(True):
    choice = int(input("Enter choice : \n Press 1 to Insert element in the Queue.\n Press 2 to delete element from the Queue.\n Press 3 to display the Queue.\n Press 0 to exit Immediately."))
    if choice == 1:
        insert(queue, int(input("\nEnter element to be Inserted in the Queue.")))
        print("Operation Completed!\n")

    elif choice == 2:
        delete(queue)
        print("\nOperation Completed!")

    elif choice == 3:
        print(display(queue))

    elif choice == 0:
        break

    else:
        print("Invalid Inputs.")
=======
def insert(queue, target):
    queue.append(target)

def delete(queue):
    queue.pop(0)

def display(queue):
    print(' '.join(map(str, queue)))


n = int(input("Enter Range :- "))
queue = [int(input("Enter {} element : ".format(i+1))) for i in range(n)]
while(True):
    choice = int(input("Enter choice : \n Press 1 to Insert element in the Queue.\n Press 2 to delete element from the Queue.\n Press 3 to display the Queue.\n Press 0 to exit Immediately."))
    if choice == 1:
        insert(queue, int(input("\nEnter element to be Inserted in the Queue.")))
        print("Operation Completed!\n")

    elif choice == 2:
        delete(queue)
        print("\nOperation Completed!")

    elif choice == 3:
        print(display(queue))

    elif choice == 0:
        break

    else:
        print("Invalid Inputs.")
>>>>>>> Python repo committed
