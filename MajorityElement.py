class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_num = len(nums) / 2

        occurences_tracker = {}

        for num in nums:
            if num in occurences_tracker:
                occurences_tracker[num] += 1
            else:
                occurences_tracker[num] = 1

        for i in occurences_tracker:
            if occurences_tracker[i] >= majority_num:
                return i
