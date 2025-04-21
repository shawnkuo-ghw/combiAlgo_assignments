# FILE: BST.py

# Node Class for Binary Search Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None 
    
    def Inorder_Walk(self):
        itr = self
        if itr is None:
            return
        else:
            if itr.left != None: 
                itr.left.Inorder_Walk()
            print(itr.key, end=" ")
            if itr.right != None:  
                 itr.right.Inorder_Walk()

    def print_bst(self, prefix: str):
        if self.right != None:
            self.right.print_bst(prefix + "    ")
        print(prefix, self.key)
        if self.left != None:
            self.left.print_bst(prefix + "    ")

# Binary Search Tree Class
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, newkey):
        newNode = Node(key=newkey)
        y = None
        x = self.root
        while x != None:
            y = x
            if newkey < x.key:
                x = x.left
            elif newkey > x.key:
                x = x.right 
            else:
                print("Duplicate Input!")
                return
        newNode.parent = y
        if y == None: # Tree is empty
            self.root = newNode
        elif newNode.key < y.key:
            y.left = newNode
        elif newNode.key > y.key:
            y.right = newNode
    
    def remove_leaf(self, tarKey):
        # z: the node to be deleted
        # p: the parent of the z
        p = None
        z = self.root
        # When the root is node to be deleted
        if self.root.key == tarKey:
            self.root = None
        # Search for the node to be deleted
        while z != None and z.key != tarKey:
            p = z
            if tarKey < z.key:
                z = z.left
            elif tarKey > z.key:
                z = z.right
        # If the node is not found, return
        if z == None:
            return
        # Delete the (leaf) node
        z.parent = None
        if p != None and p.left == z:
            p.left = None
        elif p != None and p.right == z:
            p.right = None

    def show_Inorder(self):
        print("The Inorder Walk:", end=" ")
        self.root.Inorder_Walk()
        print('\n')

    def print_BST(self):
        print("Binary Tree:")
        if self.root != None:
            self.root.print_bst("")
        print("\n")