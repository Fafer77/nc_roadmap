from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                top = stack.pop()
                snd = stack.pop()
                stack.append(operations[token](snd, top))
            else:
                stack.append(int(token))
        
        return stack[0]
    
sol = Solution()
print(sol.evalRPN(tokens=["1","2","+","3","*","4","-"]))
