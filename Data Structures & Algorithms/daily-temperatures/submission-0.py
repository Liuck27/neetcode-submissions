class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stackT = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):

            while stackT and temp > stackT[-1][1]:
                j,_ = stackT.pop()
                res[j] = i-j

            
            stackT.append([i,temp])
        
        return res
            



        
        