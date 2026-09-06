class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curSum = 0
        prefixSum = {0:1}
        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in prefixSum:
                count += prefixSum.get(diff, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return count 