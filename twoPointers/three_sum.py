from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                curr_triplet = nums[i] + nums[L] + nums[R]
                if curr_triplet > 0:
                    R -= 1
                elif curr_triplet < 0:
                    L += 1
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        
        return result
    

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
                