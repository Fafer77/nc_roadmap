from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        max_freq = 0
        char_map = defaultdict(int)

        for r in range(len(s)):
            char_map[s[r]] += 1
            if char_map[s[r]] > max_freq:
                max_freq = char_map[s[r]]
            
            if (r - l + 1) - max_freq > k:
                if s[l] == s[r]:
                    max_freq -= 1
                char_map[s[l]] -= 1
                l += 1

            max_len = max(max_len, (r - l + 1))

        return max_len