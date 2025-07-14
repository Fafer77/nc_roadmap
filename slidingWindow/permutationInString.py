from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        m = len(s1)
        shorter_map = [0] * 26
        window_map = [0] * 26

        for i in range(m):
            shorter_map[ord(s1[i]) - ord('a')] += 1
            window_map[ord(s2[i]) - ord('a')] += 1
        
        matching = 0
        for i in range(26):
            if shorter_map[i] == window_map[i]:
                matching += 1
        
        l = 0
        for r in range(m, len(s2)):
            if matching == 26:
                return True
            
            new_char = ord(s2[r]) - ord('a')
            if shorter_map[new_char] == window_map[new_char]:
                matching -= 1

            window_map[new_char] += 1

            if shorter_map[new_char] == window_map[new_char]:
                matching += 1

            old_char = ord(s2[l]) - ord('a')
            if shorter_map[old_char] == window_map[old_char]:
                matching -= 1
            
            window_map[old_char] -= 1

            if shorter_map[old_char] == window_map[old_char]:
                matching += 1

            l += 1
        
        return matching == 26

sol = Solution()
print(sol.checkInclusion('adc', 'dcda'))
