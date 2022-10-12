class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums) + 1
        for i in range(len_nums):
            if i not in nums:
                return i


# You can sum up the numbers in the array and compare it with the expected sum to find which number is missing: [n * (n+1)] / 2
