class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
        self.bal_fact = 0


class Avl:
    def __init__(self):
        self.root = None


def insert(root, data):
    if not root:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
        root.left.parent = root

    elif data > root.data:
        root.right = insert(root.right, data)
        root.right.parent = root

    root.height = get_height(root)
    root.bal_fact = get_balance_factor(root)

    if root.bal_fact > 1 and data < root.left.data:
        return right_rotate(root)

    if root.bal_fact < -1 and data > root.right.data:
        return left_rotate(root)

    if root.bal_fact > 1 and data > root.left.data:
        left_rotate(root.left)
        return right_rotate(root)

    if root.bal_fact < -1 and data < root.right.data:
        right_rotate(root.right)
        return left_rotate(root)

    return root


def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    y.parent = x.parent
    if tree.root is x:
        tree.root = y
    else:
        if x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

    x.parent = y
    return y


def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    x.parent = y.parent
    if y is tree.root:
        tree.root = x

    else:
        if y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

    y.parent = x
    return x


def search(root, tar):
    if not root and root.data == tar:
        return root

    elif tar > root.data:
        search(root.right, tar)

    elif tar < root.data:
        search(root.left, tar)


def get_height(root):
    return -1 if not root else max(1 + get_height(root.left), 1 + get_height(root.right))


def get_balance_factor(root):
    return get_height(root.left) - get_height(root.right)


def print_level_order(root):
    if not root:
        return None

    else:
        q = list()
        q.append(root)
        while len(q) > 0:

            print(q[0].data, q[0].bal_fact, q[0].height)
            node = q.pop(0)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.data, end=" ")
        print_in_order(root.right)


def print_pre_order(root):
    if root:
        print(root.data, end=" ")
        print_pre_order(root.left)
        print_pre_order(root.right)


def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.data, end=" ")


tree = Avl()
print("Enter elements in the Tree.. \n Type no to stop the Process.")
while True:
    inp = input()
    if inp.lower() in 'no':
        break
    else:
        tree.root = insert(tree.root, int(inp))

print("Elements in the Tree Using Level_Order_Traversal is :- ")
print_level_order(tree.root)
print("Element in the Tree using Pre_Order_Traversal is :- ")
print_pre_order(tree.root)
print("Element in the Tree using In_Order_Traversal is :- ")
print_in_order(tree.root)
print("Element in the Tree using Post_Order_Traversal is :- ")
print_post_order(tree.root)
