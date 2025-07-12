from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack:
                t, idx = stack[-1]
                if t < temp:
                    res[idx] = i - idx
                    stack.pop()
                else:
                    break
            stack.append((temp, i))

        return res
