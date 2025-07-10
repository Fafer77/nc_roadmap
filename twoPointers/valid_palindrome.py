class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_check_s = [char.lower() for char in s if char.isalnum()]
        n = len(to_check_s)
        for i in range(n // 2):
            if to_check_s[i] != to_check_s[n - 1 - i]:
                return False
        
        return True

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))
