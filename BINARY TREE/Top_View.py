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

def top_view(root):
    if root is None:
        return
    
    # Using a normal list as a queue (FIFO)
    queue = [(root, 0)]  # (node, horizontal_distance)
    
    # Dictionary to store first node seen at each horizontal distance
    top_nodes = {}
    
    while len(queue) > 0:
        # Remove first element (like pop from front)
        curr, hd = queue[0]
        queue = queue[1:]
        
        # If this HD is not already seen, store it
        if hd not in top_nodes:
            top_nodes[hd] = curr.data
        
        # Add left child to queue with HD - 1
        if curr.left is not None:
            queue.append((curr.left, hd - 1))
        
        # Add right child to queue with HD + 1
        if curr.right is not None:
            queue.append((curr.right, hd + 1))
    
    # Print nodes from leftmost HD to rightmost HD
    for hd in sorted(top_nodes.keys()):
        print(top_nodes[hd], end=" ")


if __name__ == "__main__":
    preorder = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]
    
    root = buildTree(preorder)
    top_view(root)
    print()
    
