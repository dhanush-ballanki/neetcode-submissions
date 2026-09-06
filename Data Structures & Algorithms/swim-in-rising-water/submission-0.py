class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        visit.add((0, 0))
        minHeap = [[grid[0][0], 0, 0]]
        directions = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if r == ROWS-1 and c == COLS - 1:
                return time
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR == ROWS or neiC == COLS or (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minHeap, [max(time, grid[neiR][neiC]), neiR, neiC])
            