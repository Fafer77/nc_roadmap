class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for curr in s:
            if curr in ['(', '{', '[']:
                stack.append(curr)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if (curr == ')' and popped == '(') or\
                    (curr == '}' and popped == '{') or\
                    (curr == ']' and popped == '['):
                    continue
                else:
                    return False

        if stack:
            return False
        else:
            return True