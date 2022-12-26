# BST needs to follow this property:
  # Everything less than the current node should be on the left side and 
  # Everything equal to or greater than the current node should be on the right side.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Average Time Complexity: O(log(n)) Space Complexity: O(1) space 
    # Worst time complexity: O(n) and Space Complexity: O(1)
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average Time Complexity: O(log(n)) Space Complexity: O(1) space 
    # Worst Time Complexity: O(n) Space Complexity: O(1)
    def contains(self, value):
        if self.value is not None and value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif self.value is not None and value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    # Average Time Complexity: O(log(n)) Space Complexity: O(1) space 
    # Worst Time Complexity: O(n) Space Complexity: O(1)
    def remove(self, value, parentNode=None):
        # You can think of removing the node as a new step process:
            # First you need to find the node 
            # Once find it, you remove it.
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # when we have two child nodes present
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    # current node is the smallest value in the right subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                
                # if root case needs to be removed
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        # If the BST only has one node and that is what needs to be removed
                        currentNode.value = None
                # only one child node or none
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                # only one child node or none
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
                break
        return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()
