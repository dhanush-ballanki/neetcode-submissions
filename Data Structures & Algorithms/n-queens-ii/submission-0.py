class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        col = set()
        nonPD = set()
        PD = set()

        res = 0
        

        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return

            for c in range(n):
                if c in col or (r + c) in nonPD or (r - c) in PD:
                    continue

                col.add(c)
                nonPD.add(r + c)
                PD.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                nonPD.remove(r + c)
                PD.remove(r - c)

        backtrack(0)
        return res