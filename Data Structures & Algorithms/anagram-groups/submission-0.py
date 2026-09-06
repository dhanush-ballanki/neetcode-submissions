class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for w in strs:
            k = ''.join(sorted(w))
            if k not in res:
                res[k] = []
            res[k].append(w)
        return list(res.values())