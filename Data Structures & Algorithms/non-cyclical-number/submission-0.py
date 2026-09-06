class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def helper(n):
            n = list(str(n))
            sqsum = 0
            for i in n:
                sqsum += int(i)*int(i)
            return sqsum
        while n != 1 and n not in seen:
            seen.add(n)
            n = helper(n)
        return n == 1