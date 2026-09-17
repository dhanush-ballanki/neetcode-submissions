class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        hmap = {}
        for a, b in zip(x, y):
            hmap[a] = max(hmap.get(a, 0), b)
        minHeap = []
        for val in hmap.values():
            heapq.heappush(minHeap, val)
            if len(minHeap) > 3:
                heapq.heappop(minHeap)
        return -1 if len(minHeap) < 3 else sum(minHeap)