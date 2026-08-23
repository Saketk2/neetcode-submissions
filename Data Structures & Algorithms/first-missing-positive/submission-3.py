class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        length = len(nums)
        while i < len(nums):
            if 0 < int(nums[i]) <= len(nums):
                nums[int(nums[i]) - 1] = str(nums[int(nums[i]) - 1])
            i += 1
        
        for index, val in enumerate(nums):
            if not isinstance(val, str):
                return index + 1

        return length + 1