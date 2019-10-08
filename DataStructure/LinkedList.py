#create Node
#create Linked List
#Add nodes to the linked list
#print linked list

#to create a node we have to create a CLASS called Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#to create a linked list we have to create a CLASS called LinkedList
class LinkedList:
    def __init__(self):
        self.head = None #an empty linked list must have its head None.

    def insert(self, newNode):  #in order to insert any  node in the Linked list we have to make sure the if our head of the linked list is empty or not.
        if self.head is None:   #if head is empty, we have to make that node to be head node.
            self.head = newNode

        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):

        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print (currentnode.data)
            currentnode = currentnode.next


#every node hava a data field and a next field
firstnode = Node("john") #object of Node Class
#firstnode.data => john and firstnode.next => None

#Now we have to create a linked list... in order to create a linked list we have to create an object of class linked list.
linkedlist = LinkedList()
#we do not pass any parameter in the linkedList() because it signifies the initallly our linked list is empty.
#And when our linked list is initally empty, we will make sure that the head of linked list is None.

linkedlist.insert(firstnode) #to insert a node into the linked list, must have a insert() method in linked list class.

secondnode = Node("Ben")
linkedlist.insert(secondnode)
thirdnode = Node("Mathews")
linkedlist.insert(thirdnode)
linkedlist.printList()