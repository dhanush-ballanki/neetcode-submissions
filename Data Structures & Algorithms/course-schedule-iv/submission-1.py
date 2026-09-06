class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, co in prerequisites:
            adj[co].append(pre)
        def dfs(co):
            if co not in preMap:
                preMap[co] = set()
                for pre in adj[co]:
                    preMap[co] |= dfs(pre)
                preMap[co].add(co)
            return preMap[co]

        preMap = {}
        for co in range(numCourses):
            dfs(co)
        res = []
        for u, v in queries:
            res.append(u in preMap[v])
        return res