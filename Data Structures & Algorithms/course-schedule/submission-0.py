class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        for co, pre in prerequisites:
            preMap[co].append(pre)
        visiting = set()
        def dfs(co):
            if co in visiting:
                return False
            if not preMap[co]:
                return True
            visiting.add(co)
            for pre in preMap[co]:
                if not dfs(pre):
                    return False
            visiting.remove(co)
            preMap[co] = []
            return True
        for co in range(numCourses):
            if not dfs(co):
                return False
        return True