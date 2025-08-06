class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i]) - 1

            while left <= right:
                mid = (right+left)//2

                if target > matrix[i][mid]:
                    left = mid + 1
                elif target < matrix[i][mid]:
                    right = mid - 1
                elif target == matrix[i][mid]:
                    return True
        
        return False
                     

        