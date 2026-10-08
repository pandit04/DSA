def twoCitySchedCost(costs):
        costs.sort(key=lambda x: x[1] - x[0])

        n = len(costs) // 2
        total = 0

        for i in range(n):
            total += costs[i][1]       

        for i in range(n, len(costs)):
            total += costs[i][0]      

        return total