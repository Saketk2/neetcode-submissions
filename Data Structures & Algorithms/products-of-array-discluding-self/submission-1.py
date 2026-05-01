class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        for i in nums[1:]:
            left.append(left[-1] * i)
        
        right = [nums[-1]]
        for i in reversed(nums[:-1]):
            right.append(right[-1] * i)
        right = right[::-1]

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(right[1])
            elif i == len(nums) - 1:
                ans.append(left[-2])
            else:
                ans.append(left[i - 1] * right[i + 1])
        return ans

        [1, 2, 8, 48]
        [48, 48, 24, 6]


        