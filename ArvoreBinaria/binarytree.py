from collections import deque

def caminho(no, profundidade):
        if no is None or no.key is None:
            return 0
        return profundidade + \
                caminho(no.left, profundidade + 1) + \
                caminho(no.right, profundidade + 1)

def inOrder(node, elems = []):
        if node.left is not None: inOrder(node.left, elems)
        elems.append(node.key)
        if node.right is not None: inOrder(node.right, elems)

def postOrder(node, elems = []):
    if node.left is not None: inOrder(node.left, elems)
    if node.right is not None: inOrder(node.right, elems)
    elems.append(node.key)

def height(node):
    if node is None: return -1
    return 1 + max(height(node.left), height(node.right))

def preOrder(node, elems = []):
    elems.append(node.key)
    if node.left is not None: inOrder(node.left, elems)
    if node.right is not None: inOrder(node.right, elems)

def isAVL(node):
    def check_balance_and_height(node):
        if node is None:
            return True, -1 

       
        left_is_avl, left_height = check_balance_and_height(node.left)
        right_is_avl, right_height = check_balance_and_height(node.right)

      
        fb = right_height - left_height
        is_balanced = -1 <= fb <= 1

      
        is_avl = is_balanced and left_is_avl and right_is_avl


        height = 1 + max(left_height, right_height)

        return is_avl, height
    return check_balance_and_height(node)[0]

class Node:
    
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None
    
    def fb(self):
        return -height(self.left) + height(self.right)    

class BinaryTree:

    def __init__(self):
        self.root = None
        self.size = 0
        self.smallest = None
        self.greatest = None
    
    def insert(self, val):
        if self.root == None: 
            self.root = Node(val)
            self.smallest = self.root.key
            self.greatest = self.root.key
        else:
            n = self.root
            while True:
                if n.key > val:
                    if n.left is None: 
                        n.left = Node(val)
                        break
                    n = n.left
                elif n.key < val:
                    if n.right is None:
                        n.right = Node(val)
                        break
                    n = n.right
                else: return
        self.size += 1
        if val < self.smallest: self.smallest = val
        if val > self.greatest: self.greatest = val

    def heightT(self):
        return self.root.height()

    def internalPathLength(self):
        return caminho(self.root, 0)

    def emOrdem(self):
        lista = []
        inOrder(self.root, lista)
        return lista
    
    def preOrdem(self):
        lista = []
        preOrder(self.root, lista)
        return lista
    
    def posOrdem(self):
        lista = []
        postOrder(self.root, lista)
        return lista
    
    def levelOrder(self):
        res = []
        if self.root is None:
            return res
        queue = deque([self.root]) 
        while queue:
            node = queue.popleft()  
            res.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res

tree = BinaryTree()
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(1)
print(tree.emOrdem(), tree.smallest, tree.greatest, tree.levelOrder(), tree.internalPathLength(), isAVL(tree.root))