class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


idx = [-1]


def buildTree(preorder):
    idx[0] += 1

    if preorder[idx[0]] == -1:
        return None

    root = Node(preorder[idx[0]])
    root.left = buildTree(preorder)
    root.right = buildTree(preorder)
    return root


def preorderTraversal(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorderTraversal(root.left)
    preorderTraversal(root.right)


def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.data, end=' ')
    inorderTraversal(root.right)


def postorderTraversal(root):
    if root is None:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data, end=' ')


if __name__ == "__main__":
    preorder = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]

    root = buildTree(preorder)

    print("Preorder Traversal:")
    preorderTraversal(root)
    print()

    print("Inorder Traversal:")
    inorderTraversal(root)
    print()

    print("Postorder Traversal:")
    postorderTraversal(root)
    print()
