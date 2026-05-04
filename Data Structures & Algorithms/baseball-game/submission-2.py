class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op.isdigit() or op.startswith('-'):
                stack.append(int(op))
            elif op == '+':
                one = stack[-1]
                two = stack[-2]
                stack.append(one + two)
            elif op == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.pop()
        return sum(stack)
        