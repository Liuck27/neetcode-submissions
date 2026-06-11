class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        # dp[i] will store the number of ways to decode s[0:i]
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # An empty string has 1 valid empty decoding
        dp[1] = 1  # A string of length 1 (not starting with '0') has 1 decoding
        
        for i in range(2, n + 1):
            # Check single digit: s[i-1]
            # (Remember, s[i-1] corresponds to the i-th character in the string)
            if s[i-1] != "0":
                dp[i] += dp[i-1]
                
            # Check two digits: s[i-2:i]
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]