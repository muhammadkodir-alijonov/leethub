from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) != len(cost):
            return -1

        total_gas = 0
        current_tank = 0
        start_index = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_gas += diff
            current_tank += diff

            if current_tank < 0:
                start_index = i + 1
                current_tank = 0

        if total_gas < 0:
            return -1

        return start_index