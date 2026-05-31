class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost) > sum(gas):
            return -1

        start = 0
        tank = gas[0]

        for i in range(1,len(gas)):

            tank -= cost[i-1]
            if tank < 0:
                start = i
                tank = gas[i]
            else:
                tank += gas[i]

        

        return start        