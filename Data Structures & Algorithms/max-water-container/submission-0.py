class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        mac = 0
        while l < r:
            mac = max(mac, (r-l)*min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mac