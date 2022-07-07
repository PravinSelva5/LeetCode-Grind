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

'''
Another Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        
        for letter in s:
            if letter not in m:
                m[letter] = 0
            m[letter] += 1
        
        for char in t:
            if char in m:
                m[char] -= 1
            else:
                m[char] = 1
        
        for char, occurence in m.items():
            if occurence != 0:
                return False
            
            
        return True


'''