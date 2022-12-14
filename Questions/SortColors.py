class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This question has a finite range [0,2], which makes it perfect for using BuckSort

        colours = [0, 0, 0]

        # We need to count the number of each colour there is.
        for color in nums:
            colours[color] += 1
        
        i = 0
        for n in range(len(colours)):
            for _ in range(colours[n]):
                nums[i] = n
                i += 1