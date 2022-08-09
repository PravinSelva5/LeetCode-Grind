# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


# Attempt Two with three different solutions
#   1. Recursive BFS
#   2. BFS - Level Order Search 
#   3. Iterative DFS  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#     # Iterative DFS answer    
#     #    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
#     # BFS - Level Order Search (DFS better for this question)
# #         level = 0
# #         q = deque([root])
        
# #         while q:
# #             # take a snapshot of the elements in the queue, remove them and replace with their children.
# #             for i in range(len(q)):
# #                 node = q.popleft()
# #                 if node.left:
# #                     q.append(node.left)
# #                 if node.right:
# #                     q.append(node.right)
    
# #             level += 1
        
# #         return level

#         stack = [[root, 1]]
#         result = 1
    
#         while stack:
#             node, depth = stack.pop()
            
#             if node:
#                 result = max(result, depth)
# # because we're not checking if it is a NULL value, the if statement will save us from entering the loop
#                 stack.append([node.left, depth + 1])
#                 stack.append([node.right, depth + 1])
            
#         return result
                