class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        nums = sorted(freq.keys(), key = lambda x: freq[x], reverse=True)
        return nums[:k]