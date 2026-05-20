class Solution:
    def countBits(self, n: int) -> List[int]:

        def countB(n):
            count = 0
            while n:
                count += n%2
                n = n // 2
            return count

        result = [0] * (n+1)

        for num in range(n+1):
            result[num] = countB(num)

        return result
        