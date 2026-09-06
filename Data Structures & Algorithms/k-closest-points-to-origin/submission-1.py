class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap = [[(p[0]**2 + p[1]**2), p[0], p[1]] for p in points]
        # heapq.heapify(heap)
        # res = []
        # for _ in range(k):
        #     res.append(heapq.heappop(heap)[1:])
        # return res

        res = sorted(points, key = lambda p: p[0]**2 + p[1]**2)
        return res[:k]
        