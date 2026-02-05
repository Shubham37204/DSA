class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def allPaths(root, path, ans):
    if root is None:
        return

    # add current node value to the path
    path = path + str(root.data)

    # if it's a leaf node → save the path
    if root.left is None and root.right is None:
        ans.append(path)
        return

    # otherwise, go left and right
    allPaths(root.left, path + "->", ans)
    allPaths(root.right, path + "->", ans)

def binaryTreePaths(root):
    ans = []
    allPaths(root, "", ans)
    return ans


# Example usage
if __name__ == "__main__":
    # build tree: [1,2,3,null,5]
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)

    print(binaryTreePaths(root))
