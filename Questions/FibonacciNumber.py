class Solution:
    def fib(self, n: int) -> int:

        # Base case
        if n <= 1:
            return n

        # Recursive Solution
        return self.fib(n - 1) + self.fib(n - 2)