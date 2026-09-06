class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        su = sum(nums)
        return (len(nums)*(len(nums)+1))//2 - su