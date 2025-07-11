from typing import List

"""
O(n) time + O(n) memory:
Idea is to store prefix maximums and suffix maximums. It allows
us to calculate for particular position what amount of water can be trapped there.
We use min(H_r, H_l) - height[i] to calculate how much water can be trapped on particular
position. There is nothing higher to the left and to the right so no more can be trapped.

O(n) time + O(1) memory optimization
the trick is that we store maxL and maxR and move one which value is lower.
Why? Because it guarantees that on another side max height is at least the same
or higher so we have guaranteed that on position we are considering if there can be water
based on one side, on another one it will also fit (because there is at least the same height)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n
        mini_height = [0] * n

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i - 1])
        
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i + 1])
        
        for i in range(n):
            mini_height[i] = min(prefix_max[i], suffix_max[i])
        
        res = 0
        for i in range(n):
            res += max((mini_height[i] - height[i], 0))

        return res
    
    def trap_optimized(self, height: List[int]) -> int:
        n = len(height)
        L = 0
        R = n - 1
        maxL = height[L]
        maxR= height[R]

        res = 0

        while L < R:
            if maxL < maxR:
                L += 1
                res += max(maxL - height[L], 0)
                maxL = max(maxL, height[L])
            else:
                R -= 1
                res += max(maxR - height[R], 0)
                maxR = max(maxR, height[R])
        
        return res