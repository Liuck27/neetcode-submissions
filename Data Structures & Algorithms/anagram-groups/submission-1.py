class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        d = defaultdict(list)

        for word in strs:
            d["".join(sorted(word))].append(word)

        return list(d.values())
        