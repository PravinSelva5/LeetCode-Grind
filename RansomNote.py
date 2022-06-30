class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        constructMap = {}

        for i in magazine:
            if i in constructMap:
                constructMap[i] += 1
            else:
                constructMap[i] = 1

        for char in ransomNote:
            if char not in constructMap:
                return False

            if constructMap[char] <= 0:
                return False

            constructMap[char] -= 1

        return True
