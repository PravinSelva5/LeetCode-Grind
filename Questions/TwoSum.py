class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        
        for num in range(len(nums)):
            valueToFind = target - nums[num]
            if (nums[num] in m):
                valueToFindIndex = m[nums[num]]
                return[valueToFindIndex, num]
            
            m[valueToFind] = num