class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        max_len = 0
        l = 0
        hash_map = {}
        for r in range(n):
            curr = s[r]
            if curr in hash_map and hash_map[curr] >= l:
                l = hash_map[curr] + 1
            
            hash_map[curr] = r
            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
        
        return max_len

    
sol = Solution()
print(sol.lengthOfLongestSubstring('pwwkew'))
