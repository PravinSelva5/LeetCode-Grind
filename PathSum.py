# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasSum(self, root, sum1, current):

        if root is None:
            return False

        current += root.val

        if root.left is None and root.right is None and current == sum1:
            return True

        return self.hasSum(root.right, sum1, current) or self.hasSum(
            root.left, sum1, current
        )

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasSum(root, targetSum, 0)
