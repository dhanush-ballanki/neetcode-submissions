class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        r_queue, d_queue = [], []
        for idx, val in enumerate(senate):
            if val == 'R':
                r_queue.append(idx)
            else:
                d_queue.append(idx)
        r_queue, d_queue = deque(r_queue), deque(d_queue)
        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r < d:
                r_queue.append(r + len(senate))
            else:
                d_queue.append(d + len(senate))
        return 'Radiant' if r_queue else 'Dire'
