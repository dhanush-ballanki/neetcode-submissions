from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        n = len(s)

        q = deque([0])
        visited = [False] * n
        visited[0] = True

        far = 0

        while q:
            i = q.popleft()

            if i == n - 1:
                return True

            start = max(i + minJump, far + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):
                if s[j] == '0' and not visited[j]:
                    visited[j] = True
                    q.append(j)

            far = end

        return False