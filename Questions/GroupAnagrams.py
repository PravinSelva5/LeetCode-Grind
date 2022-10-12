class Solution:
    def findHash(self, s):
        return ''.join(sorted(s))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagram_map = {}
        
        for s in strs:
            hashed = self.findHash(s)
            if (hashed not in anagram_map):
                anagram_map[hashed] = []
            anagram_map[hashed].append(s)
        
        for p in anagram_map.values():
            output.append(p)
        
        return output