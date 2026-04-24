class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = min(strs)
        big = max(strs)

        for i in range(len(small)):
            if big[i] != small[i]:
                return small[:i]
        return small
        