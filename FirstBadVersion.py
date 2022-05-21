# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        middle = start + (end - start) // 2

        while end > start:
            middle = start + (end - start) // 2
            if not isBadVersion(middle):
                start = middle + 1
            else:
                end = middle

        return start
