class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if  (mid == 0 and nums[0]>nums[1]) or (mid == n-1 and nums[-1] > nums[-2]) or (nums[mid-1] < nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid-1] > nums[mid]:
                r = mid-1
            else:
                l = mid+1
        