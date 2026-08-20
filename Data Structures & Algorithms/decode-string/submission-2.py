class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for val in s:
            if val != "]":
                stack.append(val)
            else:
                value = ""
                times = ""
                while stack and stack[-1] != "[":
                    value = stack.pop() + value
                stack.pop()
                while stack and stack[-1].isdigit():
                    times = stack.pop() + times
                
                stack.append(int(times) * value)
        return "".join(stack)

