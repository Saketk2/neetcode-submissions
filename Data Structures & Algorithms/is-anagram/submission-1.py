class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = [0] * 26
        t_map = [0] * 26
        for i in range(len(s)):
            curr = ord(s[i]) - ord('a')
            s_map[curr] += 1

            curr = ord(t[i]) - ord('a')
            t_map[curr] += 1
        
        return True if s_map == t_map else False

        
        