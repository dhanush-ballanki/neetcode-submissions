class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        sentence = []
        words = set(wordDict)
        def backtrack(i):
            if i == len(s):
                res.append(' '.join(sentence))
                return
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in words:
                    sentence.append(w)
                    backtrack(j+1)
                    sentence.pop()
        backtrack(0)
        return res