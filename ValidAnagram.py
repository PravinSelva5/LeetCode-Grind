class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        letters = {}

        for char in s:

            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

        for char in t:
            if char in s and letters[char] != 0:
                letters[char] -= 1
                continue
            else:
                return False

        return True
