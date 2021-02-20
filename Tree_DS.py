print("*************TREE*****************\n")
class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.v=val

class Tree:
    def __init__(self):
        self.root= None

    def getRoot(self):
        return self.root

    def add(self,val):
        if self.root is None:
            self.root=Node(val)
        else:
            self._add(val,self.root)
    def _add(self, val,node):
        if val<node.v:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left=Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right=Node(val)
                    
    def find(self,val):
        if self.root is not None:
            return self._find(val,self.root)
        
    def _find(self, val, node):
        if val==node.v:
            print('----------------------------------')
            print('|      ***Found the value***     |')
            print('----------------------------------')
        elif val<node.v and node.left is not None:
            self._find(val,node.left)
        elif val>node.v and node.right is not None:
            self._find(val,node.right)
        else:
            print('----------------------------------')
            print('|      ***NOT FOUND***     |')
            print('----------------------------------')

    def deleteTree(self):
        self.root=None
        print('----------------------------------')
        print('|      ***Tree is deleted***     |')
        print('---------------//\\---------------')

    def printTree(self):
        if self.root is not None:
            print('----------------------------------')
            print('|         ***Tree value***       |')
            print('---------------//\\---------------')
            self._printTree(self.root)
            print('----------------------------------')

    def _printTree(self,node):
        if node is not None:
            self._printTree(node.left)
            print('|             ',str(node.v),'                |')
            self._printTree(node.right)

tree= Tree()
while True:
    print('----------------------------------')
    print('|         1. Add Elements        |')
    print('|         2. SEarch Elements     |')
    print('|         3. Print TREE          |')
    print('|         4. Delets Elements     |')
    print('----------------------------------')
    choice=int(input('Enter the choice: '))
    if choice == 1:
               val=int(input("Enter the tree element: "))
               tree.add(val)
    elif choice== 2:
               val=int(input("Enter the value to Search:"))
               tree.find(val)
    elif choice== 3:
               tree.printTree()
    elif choice== 4:
               tree.deleteTree()
               break
    else:
        print('----------------------------------------------------')
        print('|  Choice is invalid. KIndly select the right one  |')
        print('----------------------------------------------------')
