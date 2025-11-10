from functools import lru_cache

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        k = 0
        while 2**k <= n:
            k += 1
        k -= 1

        return 2**(k + 1) - 1 - self.minimumOneBitOperations(2**k ^ n)
    
    def minimumOnebitOperationsDP(self, n: int) -> int:
        @lru_cache(None)
        def f(x):
            if x == 0:
                return 0
            k = x.bit_length() - 1
            p = 1 << k
            if x == p:
                return (1 << (k + 1)) - 1
            return f(p) - f(x - p)

        return f(n)