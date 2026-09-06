class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        l, r = 0, 0
        seen = set()
        while l <= r and r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxl = max(maxl, r-l + 1)
            r += 1
        return maxl