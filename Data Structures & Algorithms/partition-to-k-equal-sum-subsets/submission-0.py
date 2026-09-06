class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        l = total // k
        nums.sort(reverse = True)
        if nums[0] > l:
            return False
        sums = [0]*k
        def dfs(i):
            if i == len(nums):
                return True
            for s in range(k):
                if sums[s] + nums[i] <= l:
                    sums[s] += nums[i]
                    if dfs(i+1):
                        return True
                    sums[s] -= nums[i]
                if sums[s] == 0:
                    break
            return False
        return dfs(0)