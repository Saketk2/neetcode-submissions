class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = Counter(nums)
        for key, value in data.items():
            if value > len(nums) // 2:
                return key
        
        