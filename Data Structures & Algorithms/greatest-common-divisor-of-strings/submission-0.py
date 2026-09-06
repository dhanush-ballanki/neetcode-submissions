class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ''
        if not str1 + str2 == str2 + str1:
            return res
        return str1[:math.gcd(len(str1), len(str2))]