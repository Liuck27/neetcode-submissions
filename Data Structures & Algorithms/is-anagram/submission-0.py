class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        my_map1 = {}
        my_map2 = {}

        for item in s:
            if item not in my_map1:
                my_map1[item] = 1
            else:
                my_map1[item] += 1

        for item in t:
            if item not in my_map2:
                my_map2[item] = 1
            else:
                my_map2[item] += 1

        return my_map1 == my_map2


        