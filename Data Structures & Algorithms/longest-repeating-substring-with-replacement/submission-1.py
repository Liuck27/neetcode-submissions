class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter

        def is_valid(counter):
            counts = list(counter.values())
            counts.remove(max(counts))

            return sum(counts) <=k

        maxL = 0

        l = 0
        c = Counter()

        for r in range(len(s)):
            c[s[r]] +=1

            while not is_valid(c):
                c[s[l]] -=1
                l+=1

            maxL = max(maxL,r-l+1)


        return maxL