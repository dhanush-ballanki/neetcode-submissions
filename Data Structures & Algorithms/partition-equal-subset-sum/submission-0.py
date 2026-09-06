class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        target = total//2
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            shortDp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                shortDp.add(t)
                shortDp.add(t + nums[i])
            dp = shortDp
        return False