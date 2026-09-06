class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        r = 0
        for l in s:
            if r >= len(t):
                return 0
            if l == t[r]:
                r += 1
        return len(t) - r