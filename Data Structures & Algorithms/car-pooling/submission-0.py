class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        currCap = 0
        minHeap = []
        trips.sort(key=lambda t: t[1])
        for t in trips:
            numP, frm, to = t
            while minHeap and minHeap[0][0] <= frm:
                currCap -= minHeap[0][1]
                heapq.heappop(minHeap)
            currCap += numP
            heapq.heappush(minHeap, (to, numP))
            if currCap > capacity:
                return False
        return True
