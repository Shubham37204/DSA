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

def kth_level(root, k):
    # If the tree is empty
    if root is None:
        return
    
    # If we reach the desired level
    if k == 1:
        print(root.data, end=" ")
        return
    
    # Recur for left and right subtrees with level decreased by 1
    kth_level(root.left, k - 1)
    kth_level(root.right, k - 1)


if __name__ == "__main__":
    preorder = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]
    
    root = buildTree(preorder)
    kth_level(root)
    print()
    
