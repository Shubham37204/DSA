class Node:
    def __init__(self, val):
        self.data = val
        self.left: Node | None = None
        self.right: Node | None = None

idx = [-1]
def buildTree(preorder):
    idx[0] += 1
    if preorder[idx[0]] == -1:
        return None
    root = Node(preorder[idx[0]])
    root.left = buildTree(preorder)   
    root.right = buildTree(preorder)  
    return root

def LCA(root, p, q):
    if root is None:
        return
    
    if root.data == p or root.data == q:  # Changed here
        return root
    
    leftLCA = LCA(root.left, p, q)
    rightLCA = LCA(root.right, p, q)

    if leftLCA and rightLCA:
        return root
    elif leftLCA is not None:
        return leftLCA
    else:
        return rightLCA

if __name__ == "__main__":
    preorder = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]
    
    root = buildTree(preorder)
    ans = LCA(root, 3, 4) 
    print(ans.data if ans else None)
