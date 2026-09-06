class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        freq = Counter(hand)
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)
        while minHeap:
            low = minHeap[0]
            for i in range(low, low + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if minHeap[0] != i:
                        return False
                    heapq.heappop(minHeap)
        return True
