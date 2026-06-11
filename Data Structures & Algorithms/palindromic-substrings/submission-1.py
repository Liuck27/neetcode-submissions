class Solution:
    def countSubstrings(self, s: str) -> int:

        def reversed_string(a_string):
            return a_string[::-1]

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j] == reversed_string(s[i:j]):
                    res += 1

        return res

        