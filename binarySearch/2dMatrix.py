from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        m = len(matrix)
        l = 0
        r = m - 1
        # finding row
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                row = mid
                l = mid + 1
            else:
                return True
        
        if row == -1 or target > matrix[-1][-1]:
            return False

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
        
    
sol = Solution()
print(sol.searchMatrix(matrix = [[1,3]], target = 3))

