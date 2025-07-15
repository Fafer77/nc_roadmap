"""
Solution 1: O(nlogk) time complexity
We want each time to have easy access to maximum element in current window. In order
to achieve what we can use is maxheap - O(1) access time to maximum. But it would be hard to know
which values are still in our window and which are not.
That's why we will use maxheap but its element will be pair (value, idx). At each iteration we're going
to add new pair and take maximum CANDIDATE. If its index is below our left window border it will be popped
and we will check for new candidate

Solution 2: O(n) time complexity
We will use deque. It's going to be monotonic decreasing, so first element will always be maximum.
We will store index in it, but it will be monotonic based on values at index positions.
When adding new value we consider if it is bigger than elements from the right end of deque.
IF it is bigger then we pop values as long as there is bigger or queue is empty, because this one is further
so previous ones (smaller) will be of no use to us. 
If it is smaller we just add it to the right end.
Now we have to check whether first value in queue is still in bound, so compare it's index with l (
left border of window)
"""

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()
        l = r = 0

        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()
            
            if (r + 1) >= k:
                result.append(nums[dq[0]])
                l += 1
            r += 1
        
        return result

