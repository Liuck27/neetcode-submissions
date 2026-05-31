class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        c = Counter(nums)
        return [elem[0] for elem in c.most_common(k)]
        