class Solution:
    # Time complexity for this answer is O(n)
    # Space complexity is O(1) [all memory used is constant]
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        max_area = 0 
        
        while (left_ptr < right_ptr):
            area = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            max_area = max(area, max_area)
            
            if (height[right_ptr] < height[left_ptr]):
                right_ptr -= 1
            
            else:
                left_ptr += 1
        
        return max_area
        