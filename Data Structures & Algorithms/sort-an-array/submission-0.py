class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        curr = 0
        while curr < len(nums):
            index = curr
            for i in range(curr, len(nums)):
                if nums[i] < nums[index]:
                    index = i
            nums[curr], nums[index] = nums[index], nums[curr]
            curr += 1
        return nums

        