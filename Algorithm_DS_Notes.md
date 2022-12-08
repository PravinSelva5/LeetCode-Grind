# Algorithm & DS Notes - NeetCode

Tags: Course

# Trees

## Binary Tree

- Binary Trees don’t have any cycles in them.
- Depth for BT refers to the path from a specified node to the root node

```python
class TreeNode:
		def __init__(self, val):
				self.val = val
				self.left = None
				self.right = None

```
![Untitled 1](https://user-images.githubusercontent.com/25359882/206069362-f79bc1a0-d17e-45c5-872b-69a9292ac4aa.png)

## Binary Search Trees (BST)

- Very similar to a binary tree but have a sorted property
- For every single node, every left node subtree will have to be less than the root value & every node in the right subtree will have to be greater than the root node value.

![Untitled 2](https://user-images.githubusercontent.com/25359882/206069379-7d3936cf-3de2-4fa2-b599-bfb3c64e1cd2.png)

```python
# O(log(n)) if tree is balanced
# O(n) in the worst case if the tree isn't balanced
# O(log(n)) for inserting & deleting 
def search(root, target):
		# Base case if the root node is NULL
		if not root:
				return False

		if target > root.val:
				return search(root.right, target)
		elif target < root.val:
				return search(root.left, target)
		else:
				return True
```

- Search In A Binary Search Tree
    
    ```python
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if root is None or root.val == val: 
                return root
            return self.searchBST(root.left,val) if root.val > val else self.searchBST(root.right,val)
    ```
    

## BST Insert and Remove

- Insert

![CamScanner_10-31-2022_08 50_1](https://user-images.githubusercontent.com/25359882/206070005-4c6af557-c1c6-4d28-9017-c189694bd6e5.jpg)


- Insert into a Binary Search Tree
    
![Untitled 3](https://user-images.githubusercontent.com/25359882/206070031-9d5bab32-61c8-4aaa-b0c8-24b35a43f747.png)
    
    ```python
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            
            # base case if tree is empty
            if not root:
                return TreeNode(val)
            
            if val > root.val:
                root.right = self.insertIntoBST(root.right, val)
            
            elif val < root.val:
                root.left = self.insertIntoBST(root.left, val)
            
            return root
    ```
    
- Remove
    
![CamScanner_10-31-2022_09 22_1](https://user-images.githubusercontent.com/25359882/206070057-74ad20ef-559d-4d15-848c-a74f170880c7.jpg)
    

![CamScanner_10-31-2022_10 44_1](https://user-images.githubusercontent.com/25359882/206070112-423f208c-6a31-4108-88da-efa5b2cf93e8.jpg)

1. Delete Node in a BST
    
    ![Untitled 4](https://user-images.githubusercontent.com/25359882/206070151-9913c339-1005-4bbb-bca9-d8a95f7a08f0.png)
    
    ```python
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
    		# finding the minimum in the right subtree to keep BST 
        # this can also be written to find the maximum value in the left subtree
        def minValueNode(self, root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        def deleteNode(self, root, key):
            # Base case when the current root is Null
            if not root:
                return None
            
            # Search for value to remove
            if key > root.val:
                root.right = self.deleteNode(root.right, key)
            
            elif key < root.val:
                root.left = self.deleteNode(root.left, key)
                
            else:
                # If node only has a right child
                if not root.left:
                    return root.right
                
                # If node only has a left child
                elif not root.right:
                    return root.left
                
                else:
                    # Node has a left & right children
                    minNode = self.minValueNode(root.right)
                    
                    root.val = minNode.val
                    
                    # Remove the duplicate lowest value
                    root.right = self.deleteNode(root.right, minNode.val)
            
            return root
    ```
    
    ## Depth-First Search
    
    - Typo in the pre-order screenshot, should be `root.left` first.
    
    ![CamScanner_11-02-2022_18 52_1](https://user-images.githubusercontent.com/25359882/206070220-15193caa-dd77-47b9-ae6d-6559dcd59045.jpg)
    
    ![Untitled 5](https://user-images.githubusercontent.com/25359882/206070235-d74ee027-ee31-4cce-9a15-1502dc84665a.png)
    
    ![Untitled 6](https://user-images.githubusercontent.com/25359882/206070258-4e362378-a2c3-415f-966d-4938739e8bc7.png)
    
    ![CamScanner_11-02-2022_18 43_1](https://user-images.githubusercontent.com/25359882/206070293-3942a645-87a7-45f1-bab8-22776f6ba0ea.jpg)
    
    1. Binary Tree Inorder Traversal
        
        ![Untitled 7](https://user-images.githubusercontent.com/25359882/206070317-e1654182-af3a-4ebf-a10d-41d00ed8ab05.png)
        
        - Recursive Solution
        
        ```python
        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
        
        # O(n) for both time & space complexity
        class Solution:
            def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
                output = []
                
        				# nested function to build result
                def inorder(root):
        						# Recursive algorithm, this is the base case (1)
                    if not root:
                        return
        
                    inorder(root.left)
                    output.append(root.val)
                    inorder(root.right)
                
                
                inorder(root)
                
                return output
        ```
        
        - Iterative Solution
        
        ```python
        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
        class Solution:
            def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
                res = []
                stack = []
                cur = root
                
                while cur or stack:
                    while cur:
                        stack.append(cur)
                        cur = cur.left 
                    cur = stack.pop()
                    res.append(cur.val)
                    cur = cur.right
                
                return res
        ```
        
    2. Kth Smallest Element in a BST
        
        ![Untitled 8](https://user-images.githubusercontent.com/25359882/206070378-0d200b59-bcb4-41ea-86cc-168adce0d97d.png)
        
        - The time complexity for this solution is O(N) because we traversed every node in the BST
        - The space complexity is also O(N) because the length of the array is equal to the number of nodes in the BST
        
        ```python
        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
        class Solution:
            def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
                
                nodeValues = []
                
                
                def findValue(root):
                    if not root:
                        return
                    
                    findValue(root.left)
                    nodeValues.append(root.val)
                    findValue(root.right)
                    
                findValue(root)
                
                return nodeValues[k-1]
        ```
        
    3. Construct Binary Tree from Preorder and Inorder Traversal
        
        ![Untitled 9](https://user-images.githubusercontent.com/25359882/206070420-abda93bb-8d94-4ecd-9f5d-0f2b3cd2ed11.png)
        
        ```python
        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
        class Solution:
            def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
                # The first value of the preorder stack will ALWAYS be the root
                '''
                Once you know the root, you can look for the root in the inorder array.
                Once you find the value, you on all the integers to the left of the root will be apart of the left subtree
                and the integers to the right of the integer will be apart of the right subtree.
                
                '''
        
                if not preorder or not inorder:
                    return None
                
                
                root = TreeNode(preorder[0])
                mid = inorder.index(preorder[0])
        
                root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
                root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
                return root
        ```
        
    
    ## Breadth First Search
    
    ![CamScanner_11-09-2022_09 11_1](https://user-images.githubusercontent.com/25359882/206070442-d30cdb7c-c7f8-4b54-8d15-e3ae63f78e9d.jpg)
    
    - Time Complexity: O(N)
    - Space Complexity: O(N)
    
    ```python
    from collections import deque #double ended queue
    
    def bfs(root):
        queue = deque()
    		
    	if root:
    	    queue.append(root)
        
        level = 0
        while len(queue) > 0:
            print("level: ", level)
            for i in range(len(queue)):
    						# First In First Out
                curr = queue.popleft()
                print(curr.val)
                # Need to check if current node has children. Adding left and then right child is best practice.
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
    ```
    
    ## BST Sets and Maps
    
    - These two data structures are usually implemented using binary search tree.
    - When a set is implemented with a BST, you can insert & remove in log(N) time.
    - sets & maps can be implemented using HashMaps & HashSets as well.
    
    ```python
    from sortedcontainers import SortedDict
    
    treeMap = SortedDict({'c': 3, 'a': 1, 'b': 2})
    ```
