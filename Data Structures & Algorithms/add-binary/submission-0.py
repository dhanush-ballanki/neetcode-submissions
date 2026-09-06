class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry = 0
        res = ''
        for i in range(max(len(a), len(b))):
            da = int(a[i]) if i < len(a) else 0
            db = int(b[i]) if i < len(b) else 0
            tot = da + db + carry
            res = str(tot % 2) + res
            carry = tot // 2
        if carry:
            res = '1' + res
        return res