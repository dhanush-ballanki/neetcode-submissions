class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curSum = 0
        for i in range(len(nums)):
            if curSum > 0:
                curSum += nums[i]
            else:
                curSum = nums[i]
            res = curSum if res < curSum else res
        return res