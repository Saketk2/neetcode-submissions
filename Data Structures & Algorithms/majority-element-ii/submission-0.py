class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        data = Counter(nums)
        ans = []
        for key, value in data.items():
            if value > target:
                ans.append(key)
        return ans
        