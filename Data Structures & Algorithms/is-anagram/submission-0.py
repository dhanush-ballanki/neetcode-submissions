class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(t) == len(s):
            return False 
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True