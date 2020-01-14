<<<<<<< HEAD
class TreeArray:
    root = 0
    l = [0]*10
    def set_Root(self, key):
        TreeArray.l.insert(0, key)

    def set_LeftChild(self, key, root):
        t = (2 * root) + 1
        if TreeArray.l[root] == 0:
            print ("Cannot set Child at {}, as no parent found.".format(root))
        else:
            TreeArray.l[t] = key

    def set_RightChild(self, key, root):
        t = (2 * root) + 2
        if TreeArray.l[root] == 0:
            print ("Cannot set Child at {}, as no parent found.".format(root))
        else:
            TreeArray.l[t] = key

    def printTree(self):
        for i in TreeArray.l:
            if i == 0:
                print("-", end=" ")
            else:
                print(i, end=" ")

tree = TreeArray()
tree.set_Root("A")
# tree.set_LeftChild("B",0)
tree.set_RightChild("C",0)
tree.set_LeftChild("D",1)
tree.set_RightChild("E",1)
tree.set_LeftChild("F",2)
=======
class TreeArray:
    root = 0
    l = [0]*10
    def set_Root(self, key):
        TreeArray.l.insert(0, key)

    def set_LeftChild(self, key, root):
        t = (2 * root) + 1
        if TreeArray.l[root] == 0:
            print ("Cannot set Child at {}, as no parent found.".format(root))
        else:
            TreeArray.l[t] = key

    def set_RightChild(self, key, root):
        t = (2 * root) + 2
        if TreeArray.l[root] == 0:
            print ("Cannot set Child at {}, as no parent found.".format(root))
        else:
            TreeArray.l[t] = key

    def printTree(self):
        for i in TreeArray.l:
            if i == 0:
                print("-", end=" ")
            else:
                print(i, end=" ")

tree = TreeArray()
tree.set_Root("A")
# tree.set_LeftChild("B",0)
tree.set_RightChild("C",0)
tree.set_LeftChild("D",1)
tree.set_RightChild("E",1)
tree.set_LeftChild("F",2)
>>>>>>> Python repo committed
tree.printTree()