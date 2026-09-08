class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for dr in logs:
            match dr:
                case '../':
                    if res: res -= 1
                case './':
                    pass
                case _:
                    res += 1
        return res
             