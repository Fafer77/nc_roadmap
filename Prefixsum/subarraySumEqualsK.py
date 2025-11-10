from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_prefix = defaultdict(int)
        count_prefix[0] = 1

        res = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            res += count_prefix[curr_sum - k]
            count_prefix[curr_sum] = 1 + count_prefix[curr_sum]
        
        return res
