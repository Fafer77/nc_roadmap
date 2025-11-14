from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            res[r1][c1] += 1
            if c2 + 1 < n:
                res[r1][c2+1] -= 1
            if r2 + 1 < n:
                res[r2+1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                res[r2+1][c2+1] += 1
        
        for r in range(n):
            for c in range(1, n):
                res[r][c] += res[r][c-1]
        
        for c in range(n):
            for r in range(1, n):
                res[r][c] += res[r-1][c]
        
        return [row[:n] for row in res[:n]]

