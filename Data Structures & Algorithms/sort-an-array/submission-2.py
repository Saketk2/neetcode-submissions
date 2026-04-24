class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            return msort(merge(arr[:mid]), merge(arr[mid:]))
        
        def msort(left, right):
            i, j = 0, 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:] or right[j:])
            return result

        return merge(nums)