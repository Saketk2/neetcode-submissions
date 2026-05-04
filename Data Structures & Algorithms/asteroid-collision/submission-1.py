class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack or a > 0 or (stack[-1] < 0 and a < 0):
                stack.append(a)
            else:
                curr = a
                while stack and stack[-1] > 0:
                    if abs(curr) == stack[-1]:
                        stack.pop()
                        curr = None
                        break
                    elif abs(curr) > stack[-1]:
                        stack.pop()
                    else:
                        curr = None
                        break
                if curr:
                    stack.append(curr)
        return stack

        