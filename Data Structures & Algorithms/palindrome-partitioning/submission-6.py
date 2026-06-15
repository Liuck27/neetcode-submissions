class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        def isPal(t):
            l,r = 0, len(t)-1
            while l<=r:
                if t[l] == t[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def backtrack(i,path):
            if i == len(s):
                res.append(path[:])
                return

            for j in range(i, len(s)):
                if isPal(s[i:j+1]):
                    path.append(s[i:j+1])
                    backtrack(j+1,path)
                    path.pop()

        backtrack(0,[])
        return res
        