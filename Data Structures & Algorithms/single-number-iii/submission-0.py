class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        dif_bit = 1
        while not (dif_bit & xor):
            dif_bit <<= 1
        a = b = 0
        for i in nums:
            if dif_bit & i:
                a ^= i
            else:
                b ^= i
        return [a, b]