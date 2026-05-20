class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_map = {}

        for num in nums:
            if num not in my_map:
                my_map[num] = 0
            my_map[num] += 1

        ordered = sorted(my_map.items(), key=lambda item: item[1], reverse=True)
        result = []
        for i in range(k):
            result.append(ordered[i][0])

        return result

        