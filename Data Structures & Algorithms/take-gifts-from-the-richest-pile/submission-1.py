import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        minHeap = [-g for g in gifts]
        heapq.heapify(minHeap)
        for i in range(k):
            gift = -1*heapq.heappop(minHeap)
            heapq.heappush(minHeap, -1*(math.floor(math.sqrt(gift))))
        return -1*sum(minHeap)