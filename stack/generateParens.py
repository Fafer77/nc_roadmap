from typing import List



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr_str, open_count, close_count):
            print(f'{curr_str} : open {open_count} : close {close_count}')
            if close_count > open_count:
                return
            
            if close_count == n and open_count == n:
                res.append(curr_str)
                return
            
            if open_count < n:
                backtrack(curr_str + '(', open_count + 1, close_count)
        
            backtrack(curr_str + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return res
    
sol = Solution()
print(sol.generateParenthesis(3))
