class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax, curmin = 0, 0
        mx, mn = nums[0], nums[0]
        total = 0
        for i in nums:
            total += i
            #curmax = max(curmax + i, i)
            if curmax > 0:
                curmax += i
            else:
                curmax = i
            #curmin = min(curmin + i, i)
            if curmin < 0:
                curmin += i
            else:
                curmin = i
            mx = curmax if curmax > mx else mx
            mn = curmin if curmin < mn else mn
        return max(total - mn, mx) if mx > 0 else mx