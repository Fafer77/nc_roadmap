from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        m = max(piles)

        l = 1
        r = m

        while l <= r:
            mid = (l + r) // 2
            hours_needed = 0
            for pile in piles:
                hours_needed += ceil(pile / mid)
            if hours_needed <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res


sol = Solution()
print(sol.minEatingSpeed([25,10,23,4], 4))
