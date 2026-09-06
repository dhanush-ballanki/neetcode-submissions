class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 1
        right = x // 2
        while left <= right:
            mid = (left + right)//2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
        return right