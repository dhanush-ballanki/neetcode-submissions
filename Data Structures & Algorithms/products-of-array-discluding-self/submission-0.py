class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for i in nums:
            if i:
                prod *= i
            else:
                zero_count += 1
        if zero_count > 1: return [0] * len(nums)
        res = [0] * len(nums)
        for i in range(len(nums)):
            if zero_count:
                res[i] = 0 if nums[i] else prod
            else:
                res[i] = prod // nums[i]
        return res
        