# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        if root is None:
            return answer

        q = deque([root])  # this method is from the collections module

        while q:
            n = len(q)
            temp = []

            for i in range(0, n):
                f = q.popleft()
                temp.append(f.val)

                if f.left is not None:
                    q.append(f.left)
                if f.right is not None:
                    q.append(f.right)

            if len(temp) > 0:
                answer.append(temp[:])
                temp.clear()

        return answer
