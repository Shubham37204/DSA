# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0  # store the diameter

        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # update diameter for current node
            self.ans = max(self.ans, left_height + right_height)
            
            # return height
            return max(left_height, right_height) + 1

        height(root)
        return self.ans
