class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        for r in range(ROWS // 2):
            matrix[r], matrix[ROWS - r - 1] = matrix[ROWS - r - 1], matrix[r]
        for r in range(ROWS):
            for c in range(r, ROWS): 
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]