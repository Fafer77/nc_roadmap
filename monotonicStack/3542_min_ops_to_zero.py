"""
Idea: Notice that we need to kind of split our list into segments. We want to be able to zero as big
segmnet as we can (minimum values in each segment). So we have counter and we increase it as
we find bigger number because it means that we will need more operation.
We can solve it using monotonic stack
"""

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = [0]
        counter = 0

        for num in nums:
            while stack[-1] > num:
                stack.pop()
            if stack[-1] < num:
                counter += 1
                stack.append(num)
        
        return counter
