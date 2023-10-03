class Node:
    def __init__(self,data):
        self.data=data
        self.right =None
        self.left=None
        
class Tree:
    def __init__(self):
        self.root=None
    def preorder(self,root):
        if root is None:
            return
        print(root.data , end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
        
    def fullnode(self,root):
        if root is None:return 0
        if root.left==None and root.right==None:
            return 0
        if (root.left!=None and root.right!=None):
            return 1 + self.fullnode(root.left) + self.fullnode(root.right)
        else:
            return 0++ self.fullnode(root.left) + self.fullnode(root.right)
    
    
    
node=Tree()
node.root=Node(6)
node.root.left=Node(5)
node.root.right=Node(7)
node.root.left.left=Node(3)
node.root.left.right=Node(4)
node.root.right.left=Node(5)
node.root.right.right=Node(8)
print(" the preorder of  tree is ")
node.preorder(node.root)
print()
k=node.fullnode(node.root)
print(k)
