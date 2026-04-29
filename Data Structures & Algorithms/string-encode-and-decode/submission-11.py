class Solution:

    def __init__(self):
        self.lengths  = []

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            self.lengths.append(len(s))
            ans += s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        start = 0
        index = 0
        while index < len(self.lengths):
            ans.append(s[start:start + self.lengths[index]])
            start += self.lengths[index]
            index += 1
        return ans
