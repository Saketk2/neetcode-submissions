class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        data = set(nums)
        for num in nums:
            if num - 1 not in data:
                curr = 1
                while num + 1 in data:
                    curr += 1
                    num += 1
                ans = max(ans, curr)
        return ans

        

        