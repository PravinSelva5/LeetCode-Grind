# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        
        def dfs(root):
            
            # height of a null tree is -1
            if not root:
                return -1 
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # 
            diameter[0] = max(diameter[0], 2 + left + right)
            
            # returning the height. We're adding 1 for the path connecting the node and its parent. 
            return 1 + max(left, right)
        
        dfs(root)
        return diameter[0]