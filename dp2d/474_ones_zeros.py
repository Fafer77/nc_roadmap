from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for s in strs:
            ones = s.count('1')
            zeros = s.count('0')
            for i in range(n, ones - 1, -1):
                for j in range(m, zeros - 1, -1):
                    dp[i][j] = max(1 + dp[i - ones][j - zeros], dp[i][j])

        return dp[-1][-1]
