from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        L = 0
        R = n - 1
        while L < R:
            area = (R - L) * (min(heights[R], heights[L]))
            max_area = max(max_area, area)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return max_area
