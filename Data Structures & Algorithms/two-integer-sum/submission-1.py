class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = defaultdict(int)
        for index, num in enumerate(nums):
            goal = target - num
            if goal in data:
                return [data[goal], index]
            else:
                data[num] = index
        return -1
        