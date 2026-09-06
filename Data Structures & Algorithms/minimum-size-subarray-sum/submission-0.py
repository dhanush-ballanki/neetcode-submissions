class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        mlen = 10**5
        su = 0
        for r in range(len(nums)):
            su += nums[r]
            while su >= target:
                mlen = min(mlen, r-l+1)
                su -= nums[l]
                l += 1
        return mlen if mlen<=len(nums) else 0
                
        