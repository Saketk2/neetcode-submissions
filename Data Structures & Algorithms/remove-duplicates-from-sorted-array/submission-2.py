class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        main = 1
        finder = 1
        while finder < len(nums):
            while finder < len(nums) and nums[finder] == nums[finder - 1]:
                finder += 1
            if not finder < len(nums):
                continue 
            nums[main] = nums[finder]
            main += 1
            finder += 1
        return main
    