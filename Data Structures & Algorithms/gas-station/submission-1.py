class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumGas = 0
        sumCost = 0
        for i in range(len(gas)):
            sumGas += gas[i]
            sumCost += cost[i]
        if sumGas < sumCost:
            return -1
        

        idx = 0
        total = 0
        for i in range(len(gas)):
            total = total + gas[i] - cost[i]
            if total < 0:
                total = 0
                idx = i + 1
        return idx