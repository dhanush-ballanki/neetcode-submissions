class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cmin, cmax = 1, 1
        for num in nums:
            tmp = max(cmax*num, cmin*num, num)
            cmin = min(cmax*num, cmin*num, num)
            cmax = tmp
            res = max(res, cmax)
        return res