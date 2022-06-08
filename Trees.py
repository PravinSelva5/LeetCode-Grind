class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


# In-order traversal, "In" refers to where the root is in relation to the left & right nodes.
# As a result, LEFT node is visited, then ROOT node, then RIGHT node


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


# Pre-order traversal, "Pre" refers to when the root node is checked.
# In this case, the traversal is ROOT LEFT RIGHT


def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


# Post-order traversal, "Post" refers to when the root node is checked.
# In this case, the traversal is LEFT RIGHT ROOT
# Essentially before printing the current/root node or marking the node as visited. Check the left and right nodes as well.


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


root = Node(4)

root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)


inorder(root)
preorder(root)
postorder(root)
