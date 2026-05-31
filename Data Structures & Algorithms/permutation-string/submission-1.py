class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        if len(s1) > len(s2):
            return False

        wl = len(s1)
        c1 = Counter(s1)
        c2 = Counter(s2[:wl])

        if c1 == c2:
            return True

        for i in range(wl, len(s2)):
            c2[s2[i - wl]] -= 1
            c2[s2[i]] += 1

            if c1 == c2:
                return True

        return False
