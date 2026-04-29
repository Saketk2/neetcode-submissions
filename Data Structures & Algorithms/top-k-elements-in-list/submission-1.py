class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        data = Counter(nums)
        for key, value in data.items():
            heapq.heappush(heap, [-value, key])
        
        ans = []
        while heap and k:
            freq, val = heapq.heappop(heap)
            ans.append(val)
            k -= 1
        return ans

        