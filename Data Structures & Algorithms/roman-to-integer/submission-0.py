class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        prev_val = 0
        for char in reversed(s):
            curr_val = roman[char]
            if curr_val < prev_val:
                res -= curr_val
            else:
                res += curr_val
            prev_val = curr_val
            
        return res