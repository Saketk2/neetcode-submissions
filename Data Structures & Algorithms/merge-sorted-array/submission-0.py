class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = len(nums1) - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[total] = nums1[m]
                m -= 1
            else:
                nums1[total] = nums2[n]
                n -= 1
            total -= 1
        
        if n >= 0:
            nums1[:n + 1] = nums2[:n + 1]

        