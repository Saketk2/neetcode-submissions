class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in '[{(':
                stack.append(p)
            elif p == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif p == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif p == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        