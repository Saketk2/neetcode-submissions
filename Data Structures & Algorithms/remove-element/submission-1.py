class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        good = 0
        bad = len(nums) - 1
        while good <= bad:
            if nums[good] == val:
                nums[good], nums[bad] = nums[bad], nums[good]
                bad -= 1
            else:
                good += 1
        nums = nums[:bad]
        return good

        
        