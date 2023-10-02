class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Binary:
    def __init__(self):
        self.root=None
        
    def preorder(self,root):
        if root is None:
            return 
        print(root.data , end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    def countnode(self,root):
        if root is None:
            return 0
        return 1 + self.countnode(root.left) + self.countnode(root.right)
    def leafnode(self,root):
        if root.left==None and root.right==None:
            return 1
        return self.leafnode(root.left)+self.leafnode(root.right)
    def nonleaf(self,root):
        if root.left==None and root.right==None:
            return 0
        return 1+self.nonleaf(root.left) + self.nonleaf(root.right)
        
        
        
tree=Binary()
tree.root=Node(5)
tree.root.left=Node(1)
tree.root.right=Node(6)
tree.root.left.left=Node(0)
tree.root.left.right=Node(2)
tree.root.right.left=Node(5)
tree.root.right.right=Node(4)
print("the preorder")
tree.preorder(tree.root)
print()
count=tree.countnode(tree.root)
print(count)
countleaf=tree.leafnode(tree.root)
print(countleaf)
