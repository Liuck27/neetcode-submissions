class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hm = defaultdict(list)
        hm["2"] = ["a", "b", "c"]
        hm["3"] = ["d", "e", "f"]
        hm["4"] = ["g", "h", "i"]
        hm["5"] = ["j", "k", "l"]
        hm["6"] = ["m", "n", "o"]
        hm["7"] = ["p", "q", "r","s"]
        hm["8"] = ["t", "u", "v"]
        hm["9"] = ["w", "x", "y","z"]

        res = []
        def backtrack(i,word):
            if i == len(digits):
                res.append(word)
                return
            
            for letter in hm[digits[i]]:
                backtrack(i+1,word+letter)

        backtrack(0,"")
        return res if digits else []
        