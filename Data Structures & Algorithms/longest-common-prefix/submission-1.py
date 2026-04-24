class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr = ""
        index = 0
        while True:
            if index < len(strs[0]):
                char = strs[0][index]
            else:
                return curr
            for s in strs[1:]:
                if len(s) <= index or s[index] != char:
                    return curr
            curr += char
            index += 1
        return curr

        