from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1 


sol = Solution()
print(sol.search([3,4,5,6,1,2], 1))
