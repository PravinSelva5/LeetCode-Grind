# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = -float("inf")

    def solution(self, node):
        if node is None:
            return 0

        left = self.solution(node.left)
        right = self.solution(node.right)

        maxSide = max(node.val, max(left, right) + node.val)
        maxTop = max(maxSide, left + right + node.val)

        self.answer = max(self.answer, maxTop)
        return maxSide

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.solution(root)
        return self.answer
