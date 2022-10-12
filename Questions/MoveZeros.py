class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Are the elements sorted? No, can't assume array elements are sorted
        # Can the entire array be filled with 0's? Yes, that is a valid test case
        ptr = 0
        search_ptr = 0
        len_arr = len(nums)

        for i in range(len_arr):
            if nums[search_ptr] != 0:
                nums[ptr] = nums[search_ptr]
                search_ptr += 1
                ptr += 1
            else:
                search_ptr += 1

        for j in range(ptr, len_arr):
            nums[ptr] = 0
            ptr += 1
