class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len (t):
            return False

        Cs = Counter(s)
        Ct = Counter(t)

        return Cs == Ct

        
        