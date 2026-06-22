class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = Counter(t)
        s_count = Counter()

        l= 0

        resL = float("inf")
        res = ""
        matches = len(t_count)

        for r in range(len(s)):

            if s[r] in t_count:
                s_count[s[r]] += 1
                if s_count[s[r]] == t_count[s[r]]:
                    matches -= 1  
            
            while matches == 0:
                if r-l+1 < resL:
                    resL = r-l+1
                    res = s[l:r+1]

                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] + 1 == t_count[s[l]]:
                        matches += 1
                l += 1


        return "" if resL == float("inf") else res

            
            

