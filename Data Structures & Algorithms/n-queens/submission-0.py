class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        nonPD = set()
        PD = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in nonPD or (r - c) in PD:
                    continue

                col.add(c)
                nonPD.add(r + c)
                PD.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                nonPD.remove(r + c)
                PD.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res