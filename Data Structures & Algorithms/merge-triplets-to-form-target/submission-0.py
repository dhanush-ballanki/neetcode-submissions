class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()
        x, y, z = target
        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            if a == x:
                found.add(0)
            if b == y:
                found.add(1)
            if c == z:
                found.add(2)

            if len(found) == 3:
                return True

        return len(found) == 3