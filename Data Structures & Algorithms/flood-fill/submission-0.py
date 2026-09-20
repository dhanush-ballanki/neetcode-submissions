class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ROWS, COLS = len(image), len(image[0])
        seen = set()
        initial = image[sr][sc]
        def dfs(r, c):
            if ((r, c) in seen or
            r < 0 or c < 0 or r >= ROWS or c >= COLS or image[r][c] != initial):
                return
            image[r][c] = color
            seen.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        dfs(sr, sc)
        return image
            
