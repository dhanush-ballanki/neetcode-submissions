class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int("".join(map(str,digits)))
        res = res + 1
        res = [int(d) for d in str(res)]
        return res