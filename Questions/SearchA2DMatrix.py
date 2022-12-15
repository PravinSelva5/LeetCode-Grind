class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search can be used because the matrix is sorted.

        left = 0
        right = len(matrix[0])
        
        i = 0
        while i < len(matrix):
            mid = (left + right) // 2

            if target not in matrix[i] or left > right:
                i += 1
            elif target > matrix[i][mid]:
                left = mid + 1
            elif target < matrix[i][mid]:
                right = mid - 1
            else:
                return True
        
        return False  