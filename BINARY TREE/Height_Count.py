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

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

def sum(root):
    if root is None:
        return 0
    return sum(root.left) + sum(root.right)+root.data


if __name__ == "__main__":
    preorder = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]

    root = buildTree(preorder)
    print(height(root))
    print(countNodes(root))
    print(sum(root))
