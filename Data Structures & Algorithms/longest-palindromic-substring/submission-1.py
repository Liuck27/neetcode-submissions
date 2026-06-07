class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = 0
        resLen = 1

        for i in range(len(s)):

            #odd length
            l = i - 1
            r = i + 1
            while l >= 0 and r<len(s) and s[l] == s[r]:
                if r-l+1>resLen:
                    resLen = r-l+1
                    res = l
                l -= 1
                r += 1

            #even length
            l = i
            r = l + 1
            while l >= 0 and r<len(s) and s[l] == s[r]:
                if r-l+1>resLen:
                    resLen = r-l+1
                    res = l
                l -= 1
                r += 1

        return s[res:res+resLen]
        