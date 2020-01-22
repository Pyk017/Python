class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def level_order_traversal(root):
    if root is None:
        return None
    else:
        q = list()
        q.append(root)
        while len(q) > 0:
            print(q[0].data, end=" ")
            p_next = q.pop(0)
            if p_next.left is not None:
                q.append(p_next.left)
            if p_next.right is not None:
                q.append(p_next.right)


class Tree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, data):
        if self.root is None:
            return Node(data)

        else:
            temp = Node(data)
            p_node = self.root
            q_node = None
            while p_node is not None:
                q_node = p_node
                if data > p_node.data:
                    p_node = p_node.right
                else:
                    p_node = p_node.left

            if data > q_node.data:
                q_node.right = temp
                temp.parent = q_node
            else:
                q_node.left = temp
                temp.parent = q_node

        return self.root

    def insert_recursive(self, root, data):
        if root is None:
            return Node(data)
        elif data < self.root.data:
            self.root.left = self.insert_recursive(self.root.left, data)
        else:
            self.root.right = self.insert_recursive(self.root.right, data)

        return self.root

    def in_order_traversal(self, root):
        if root is not None:
            self.in_order_traversal(root.left)
            print(root.data, end=" ")
            self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root is not None:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.data, end=" ")

    def double_order_traversal(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.double_order_traversal(root.left)
            print(root.data, end=" ")
            self.double_order_traversal(root.right)

    def triple_order_traversal(self, root):
        if root is not None:
            print(root.data, end=' ')
            self.triple_order_traversal(root.left)
            print(root.data, end=' ')
            self.triple_order_traversal(root.right)
            print(root.data, end=' ')

    def height(self, root):
        return -1 if root is None else max(1 + self.height(root.left), 1 + self.height(root.right))


tree_obj = Tree()
print("This is a Demonstration of Double Order Tree Traversal and I am hereby Practicing my tree implementation "
      "capabilities as well after a long time.")
while True:
    ch = (input("Enter What you want to do! \n 1. Enter 'insert' to insert data into the Tree. \n 2. Enter 'print' to "
                "print the data of the Tree in a specific manner.\n 3. Enter 'height' to calculate height of the Tree.")
          )
    if ch.lower() in 'insert':
        print("Enter elements to be inserted into the Tree :- ")
        inp = list(map(int, input().split()))
        for i in inp:
            tree_obj.root = tree_obj.insert_iterative(i)
        print("Elements inserted!")

    elif ch.lower() in 'print':
        print("Enter the order in which you want to print the data present in the Tree :- \n 1. InOrder\n 2. "
              "PreOrder\n 3. PostOrder\n 4. LevelOrder\n 5. DoubleOrder.\n 6. TripleOrder.")
        while True:
            choice = input()
            if choice.lower() in 'inorder':
                print("Tree Elements are :- ", end=' ')
                tree_obj.in_order_traversal(tree_obj.root)
            elif choice.lower() in 'preorder':
                print("Tree Elements are :- ", end=' ')
                tree_obj.pre_order_traversal(tree_obj.root)
            elif choice.lower() in 'postorder':
                print("Tree Elements are :- ", end=' ')
                tree_obj.post_order_traversal(tree_obj.root)
            elif choice.lower() in 'levelorder':
                print("Tree Elements are :- ", end=' ')
                level_order_traversal(tree_obj.root)
            elif choice.lower() in 'doubleorder':
                print("Tree Elements are :- ", end=' ')
                tree_obj.double_order_traversal(tree_obj.root)
            elif choice.lower() in 'tripleorder':
                print("Tree Elements are :- ", end=' ')
                tree_obj.triple_order_traversal(tree_obj.root)
            else:
                break

    elif ch.lower() in 'height':
        print("The Height of the Tree is :- ", tree_obj.height(tree_obj.root))
    else:
        break
