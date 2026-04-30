class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)

        def helper(word):
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord('a')] += 1
            return tuple(arr)
        
        for word in strs:
            temp = helper(word)
            data[temp].append(word)
        
        ans = []
        for value in data.values():
            ans.append(value)
        return ans
        