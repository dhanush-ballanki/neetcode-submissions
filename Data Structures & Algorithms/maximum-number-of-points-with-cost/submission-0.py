class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        row = points[0]
        for r in range(1, ROWS):
            nxtrow = points[r].copy()
            left, right = [0]*COLS, [0]*COLS
            left[0], right[COLS-1] = row[0], row[COLS-1]
            for c in range(1, COLS):
                left[c] = max(left[c-1]-1, row[c])
            for c in range(COLS-2, -1, -1):
                right[c] = max(right[c+1]-1, row[c])
            for c in range(COLS):
                nxtrow[c] += max(left[c], right[c])
            row = nxtrow
        return max(row)