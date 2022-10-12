# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST's are by default sorted. Therefore, the left subtree will always have a node less than the current node.
        # Likewise, right subtree will have a node that is greater than the current node

        self.k = k
        self.result = None

        self.inorder(root)

        return self.result

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        self.k -= 1
        if self.k == 0:
            self.result = root.val
            return

        self.inorder(root.right)
