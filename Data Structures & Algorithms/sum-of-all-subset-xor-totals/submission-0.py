class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # total = 0
        # i = 0
        # def dfs(i, total):
        #     if i == len(nums):
        #         return total
        #     return dfs(i+1, total^nums[i]) + dfs(i+1, total)
        # return dfs(i, total)
        res = 0
        for i in nums:
            res |= i
        return res << (len(nums)-1)