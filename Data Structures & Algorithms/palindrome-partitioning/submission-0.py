class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_pal(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        def backtrack(i, j, cur):
            if i >= len(s):
                if i == j:
                    res.append(cur.copy())
                return
            if is_pal(s, j, i):
                cur.append(s[j:i+1])
                backtrack(i+1, i+1, cur)
                cur.pop()
            backtrack(i+1, j, cur)
        backtrack(0, 0, [])
        return res

        