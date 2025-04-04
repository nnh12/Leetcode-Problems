class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        matrix = {}
        max_rank = 0

        for road in roads:
            if road[0] not in matrix:
                matrix[road[0]] = set()
                matrix[road[0]].add(road[1])
            else:
                matrix[road[0]].add(road[1])

            if road[1] not in matrix:
                matrix[road[1]] = set()
                matrix[road[1]].add(road[0])
            else:
                matrix[road[1]].add(road[0])
        
        for city in range(n):
            for other in range(city + 1, n):
                n1, n2 = 0, 0
                neighbor_2 = set()
                
                if city in matrix:
                    neighbor_1 = matrix[city]
                    n1 = len(neighbor_1)

                if other in matrix:
                    neighbor_2 = matrix[other]
                    n2 = len(neighbor_2)

                cur = n1 + n2
                if city in neighbor_2:
                    cur -= 1

                max_rank = max( cur, max_rank)
            
        
        return max_rank
