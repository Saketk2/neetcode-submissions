class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        data = defaultdict(int)
        data[0] = 1

        s = 0
        ans = 0
        for n in nums:
            s += n
            ans += data[s - k]
            data[s] += 1
        return ans

        