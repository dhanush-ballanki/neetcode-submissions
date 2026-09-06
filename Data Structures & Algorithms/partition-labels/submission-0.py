class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: i for i, char in enumerate(s)}

        results = []
        end = 0
        start = 0
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if end == i:
                results.append(i + 1 - start)
                start = i + 1
        return results