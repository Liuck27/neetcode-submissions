class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target = ""
        winSize = 0 
        if len(s1)<=len(s2):
            target = sorted(s1)
            winSize = len(s1)



        for i in range(len(s2)-winSize+1):
            if sorted(s2[i:i+winSize]) == target:
                return True

        return False

        
        