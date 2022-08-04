def binarySearch(arr, target):
    # returns index of target
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [1, 2, 3, 4, 5, 6]
target = 5

result = binarySearch(arr, target)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in the array.")

# --------------------------------------------- #
# Attempt 2 at Binary Search LeetCode Question  #
# --------------------------------------------- #

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         start, end = 0, len(nums) - 1
        
#         while start <= end:
#             mid = start + (end - start) // 2
            
#             if nums[mid] > target:
#                 end = mid - 1
            
#             elif nums[mid] < target:
#                 start = mid + 1
            
#             else:
#                 return mid
        
#         return -1
        