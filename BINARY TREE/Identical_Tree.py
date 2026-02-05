# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        # Base case: if both nodes are None, they are the same
        if p is None or q is None:
            return p == q
        
        # Recursive case: check if current nodes have same value
        # and recursively check left and right subtrees
        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)
        
        return isLeftSame and isRightSame and p.val == q.val

    def isSubtree(self, root, subRoot):
        if root is None or subRoot is None:
            return root==subRoot
        
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
