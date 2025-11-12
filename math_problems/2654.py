from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        # solution if there are ones
        n = len(nums)
        one_count = nums.count(1)
        
        if one_count > 0:
            return n - one_count
        
        # try finding if it is possible to make 1 with gcds
        shortest_sub_gcd_one = float('inf')
        gcd_dp = {}

        for i, num in enumerate(nums):
            next_dp = {}
            next_dp[num] = i

            for old_gcd, idx in gcd_dp.items():
                new_gcd = gcd(num, old_gcd)
                if new_gcd in next_dp:
                    next_dp[new_gcd] = max(next_dp[new_gcd], idx)
                else:
                    next_dp[new_gcd] = idx
        
            if 1 in next_dp:
                k = next_dp[1]
                curr_len = i - k + 1
                shortest_sub_gcd_one = min(shortest_sub_gcd_one, curr_len)
            
            gcd_dp = next_dp


        if shortest_sub_gcd_one == float('inf'):
            return -1
        
        return (shortest_sub_gcd_one - 1) + (n - 1)


