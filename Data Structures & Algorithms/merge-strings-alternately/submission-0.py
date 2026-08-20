class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        p1 = 0
        p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            new_string += word1[p1]
            new_string += word2[p2]
            p1 += 1
            p2 += 1
        
        if p1 < len(word1):
            new_string += word1[p1:]
        elif p2 < len(word2):
            new_string += word2[p2:]
        
        return new_string
