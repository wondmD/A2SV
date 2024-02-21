class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        tot = 0
        costs.sort(key = lambda x: x[0]-x[1])
        mid = n //2
        tot = 0
        for i in range(mid):
            tot += costs[i][0]
            tot += costs[i+mid][1]
        return tot
