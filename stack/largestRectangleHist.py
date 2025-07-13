"""
Idea is that we will consider for each rectangle in histogram potential rectangle. We know its height
because it will best just height[i], but how about width.
In order to know width we will need boundaries for left and right end of rectangle for this
particular height[i].
Boundaries will be set based on first value to the left and right which have smaller heights than
height[i], because everything between them will be width for our rectangle of height[i].
To fill both arrays we will use monotonic stack with index position =>
as long as there is something higher or equal in the stack we will be popping in because
it means we can extend i-th rectangle to the left, but if there is smaller value it is our stop.
We can't go further as we can't create rectangle anymore with height[i] because this height is smaller.
Another stop would be if stack is empty.
Similar to right border, but iterate from right to left
"""


from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_boundary = [-1] * n
        right_boundary = [n] * n

        left_stack = []
        for i in range(n):
            while left_stack and heights[left_stack[-1]] >= heights[i]:
                left_stack.pop()
            
            if left_stack:
                left_boundary[i] = left_stack[-1]
            
            left_stack.append(i)
        
        right_stack = []
        for i in range(n - 1, -1, -1):
            while right_stack and heights[right_stack[-1]] >= heights[i]:
                right_stack.pop()
            
            if right_stack:
                right_boundary[i] = right_stack[-1]
            
            right_stack.append(i)
        
        print(left_boundary)
        print(right_boundary)

        max_area = 0
        for i, height in enumerate(heights):
            curr_area = height * (right_boundary[i] - left_boundary[i] - 1)
            max_area = max(max_area, curr_area)

        return max_area
                
sol = Solution()
print(sol.largestRectangleArea([7,1,7,2,2,4]))
