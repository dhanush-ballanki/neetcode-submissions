class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxh = [-c for c in count.values()]
        heapq.heapify(maxh)

        time = 0
        q = deque()  
        while maxh or q:
            time += 1

            if not maxh:
                time = q[0][1]
            else:
                c = 1 + heapq.heappop(maxh)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxh, q.popleft()[0])
        return time