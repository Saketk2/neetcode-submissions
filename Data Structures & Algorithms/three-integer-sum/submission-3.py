class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for index, num1 in enumerate(nums):
            if index > 0 and nums[index - 1] == num1:
                continue

            left = index + 1
            right = len(nums) - 1
            while left < right:
                if num1 + nums[left] + nums[right] > 0:
                    right -= 1
                elif num1 + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    ans.append([num1, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ans


            
        