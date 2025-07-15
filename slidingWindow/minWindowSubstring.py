"""
Idea is to use hash map to check whether current substring includes all letters of t in O(1) time.
Use sliding window and extend it to the right as long as not all chars from t are in current substring.
Once there are, move left border of window and try making window smaller. Update every time it was successful.
When char is either deleted or added update match value and window_map accordingly.
"""

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        unique_chars_t = sum(1 for c in t_map.values() if c > 0)
        window_map = defaultdict(int)
        match = 0
        min_len = float('inf')
        min_l = -1
        min_r = -1

        l = 0
        r = -1
        while r < len(s) - 1:
            r += 1

            new_char = s[r]
            window_map[new_char] += 1
            if window_map[new_char] == t_map[new_char]:
                match += 1

            # moving left window border
            while match == unique_chars_t:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_l = l
                    min_r = r
                old_char = s[l]
                if old_char in t_map.keys() and window_map[old_char] == t_map[old_char]:
                    match -= 1
                window_map[old_char] -= 1
                l += 1
        
        return s[min_l:min_r + 1] if min_r != -1 else ""
            
            
sol = Solution()
print(sol.minWindow('xyz', 'xyz'))
