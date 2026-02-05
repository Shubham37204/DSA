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

def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)


def SumTree(root):
    if root is None:
        return 0
    
    leftSum = SumTree(root.left)
    rightSum = SumTree(root.right)
    root.data+=leftSum+rightSum
    return root.data

if __name__ == "__main__":
    preorder_list = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]
    root = buildTree(preorder_list)
    print("Before SumTree:")
    preorder(root)
    print()
    ans = SumTree(root)
    print(f"\nTotal Sum of Tree: {ans}")

    print("\nAfter SumTree:")
    preorder(root)
    print()
    
