from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        output = []

        # add root node to queue
        if root:
            queue.append(root)

        
        while queue:
            qLen = len(queue)
            level = []

            for i in range(qLen):
                curr = queue.popleft()
                
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if level:
                output.append(level)
        
        return output
                
