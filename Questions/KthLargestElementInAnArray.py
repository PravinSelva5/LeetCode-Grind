# This is the quicksort solution but can't pass the leetcode test cases
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # to get time complexity O(n) on average, is QuickSelect
        # similar to quicksort,
        k = len(nums) - k

        def quickSelect(start, end):
            pivot = nums[end]
            left = start

            for i in range(start, end):
                if nums[i] <= pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            
            # Swap the pivot value with where the left pointer.
            # At this point, we know that everything to the left will be less than the pivot value.
            # Now we can check if the kth value is to the left or right of the pivot value.
            nums[end], nums[left] = nums[left], pivot
            

            if nums[k] > pivot:
                return quickSelect(left+1,end)
            elif nums[k] < pivot:
                return quickSelect(0,left-1)
            else:
                return nums[k]
            
        return quickSelect(0, len(nums) - 1)