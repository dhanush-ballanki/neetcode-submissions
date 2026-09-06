class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            fl = (heapq.heappop(heap))
            sl = (heapq.heappop(heap))
            if fl < sl:
                heapq.heappush(heap, (fl-sl))
        return abs(heap[0]) if heap else 0
            