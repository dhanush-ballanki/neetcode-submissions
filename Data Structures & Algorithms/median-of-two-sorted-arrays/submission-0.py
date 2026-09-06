class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        so = nums1+nums2
        so.sort()
        n = len(so)
        if n%2 == 0:
            return (so[(n-1)//2] + so[n//2])/2
        else:
            return so[n//2]