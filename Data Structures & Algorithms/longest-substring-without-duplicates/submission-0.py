class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0

        if len(s) == 0:
            return max_len

        l=0
        r=l+1
        hset = set()
        hset.add(s[l])
        max_len = 1

        while r < len(s):
            
            while s[r] in hset:
                hset.remove(s[l])
                l +=1

            hset.add(s[r])
            max_len = max(max_len,r-l+1)
            r +=1
            

        return max_len
    
        