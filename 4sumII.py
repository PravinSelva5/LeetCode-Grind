class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m = {}
        answer = 0
        lA = len(nums1)
        lB = len(nums2)
        lC = len(nums3)
        lD = len(nums4)
        
        for i in range(0, lA):
            x = nums1[i]
            for j in range(0, lB):
                y = nums2[j]
                
                if (x+y not in m):
                    m[x+y] = 0
                
                m[x+y] += 1
        
        for i in range(0, lC):
            x = nums3[i]
            for j in range(0, lD):
                y = nums4[j]
                target = -(x+y)
                if (target in m):
                    answer += m[target]
        
        return answer
        