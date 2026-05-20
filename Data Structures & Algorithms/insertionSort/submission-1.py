# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        solution = [pairs.copy()]
        for i in range(1, len(pairs)):
            k=0
            while (pairs[i].key >= pairs[k].key and k<i):
                k += 1
            temp = pairs.pop(i)
            pairs.insert(k, temp)
            solution.append(pairs.copy())

        return solution

                
        