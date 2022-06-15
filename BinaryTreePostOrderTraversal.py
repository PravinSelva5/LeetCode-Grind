# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Solution with Stack Implementation
        
        if (not root):
            return
        
        answer = [] 
        st1 = []
        st2 = []
        
        
        st1.append(root)
        
        while(st1):
            x = st1[-1]
            st1.pop()
            st2.append(x)
            
            if(x.left):
                st1.append(x.left)
                
            if(x.right):
                st1.append(x.right)
        
        
        while(st2):
            y = st2[-1]
            st2.pop()
            answer.append(y.val)
        
        return answer