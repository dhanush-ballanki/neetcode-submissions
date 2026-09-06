class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        maxh = [[-cnt, char] for char, cnt in c.items()]
        res = ''
        heapq.heapify(maxh)
        prev = None
        while maxh or prev:
            if prev and not maxh:
                return ""
            cnt, char = heapq.heappop(maxh)
            cnt += 1
            res += char
            if prev:
                heapq.heappush(maxh, prev)
                prev = None
            if cnt < 0:
                prev = [cnt, char]
        return res
