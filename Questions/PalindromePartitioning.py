# Palindrome is a word, sentence, or verse that reads the same forward or backward
# Backtracking is the exhaustive search part, we look at every possible case during this search. In Dynamic Programming,
# you would be storing previous sub-problems solutions so that we can use them again in the future sub problem.


class Solution:
    def isPalin(self, seg):
        i = 0
        j = len(seg) - 1

        while i < j:
            if seg[i] != seg[j]:
                return False
            i += 1
            j -= 1
        return True

    def dfs(self, s: str):
        if len(s) == 0 and len(self.temp) > 0:
            self.result.append(self.temp[:])
            return
        n = len(s) + 1
        for i in range(1, n):
            seg = s[0:i]
            if self.isPalin(seg):
                self.temp.append(seg)
                self.dfs(s[i:])
                self.temp.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.temp = []

        self.dfs(s)
        return self.result
