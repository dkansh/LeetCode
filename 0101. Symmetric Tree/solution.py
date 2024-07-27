# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None or left.val != right.val:
            return False
        return self.helper(left.right, right.left) and self.helper(left.left, right.right)
        