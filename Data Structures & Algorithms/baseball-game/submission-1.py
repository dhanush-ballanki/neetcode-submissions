class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for sc in operations:
            if sc == 'C':
                res.pop()
            elif sc == 'D':
                res.append(res[-1]*2)
            elif sc == '+':
                res.append(res[-1]+res[-2])
            else:
                res.append(int(sc))
        return sum(res)
