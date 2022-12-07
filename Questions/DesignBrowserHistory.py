class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        # pointer tracking the current URL
        self.current = self.head

    def visit(self, url: str) -> None:
        # create a node with the new url
        node = Node(url)

        node.prev = self.current
        node.next = None

        self.current.next = node
        self.current = node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev is not None:
                self.current = self.current.prev
        return self.current.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next is not None:
                self.current = self.current.next
        return self.current.val