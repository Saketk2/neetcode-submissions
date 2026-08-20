class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hit = set(nums)
        ans = len(hit)
        main = 0
        finder = 0
        while finder < len(nums):
            while finder < len(nums) and nums[finder] not in hit:
                finder += 1
            if not finder < len(nums):
                continue 
            nums[main] = nums[finder]
            hit.remove(nums[main])
            main += 1
        return ans
    