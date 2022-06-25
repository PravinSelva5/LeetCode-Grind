# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, root):
        if root == None:
            return

        else:
            temp = root

            # recursive calls
            self.invert(root.left)
            self.invert(root.right)

            # swap direction
            temp = root.left
            root.left = root.right
            root.right = temp

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return

        self.invert(root)

        return root
