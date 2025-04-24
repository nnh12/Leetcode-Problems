class Solution(object):

    def __init__(self):
        self.matrix = defaultdict(list)

    def dfs(self, node, thres, n):
        heap = []
        heapq.heapify(heap)
        
        heapq.heappush(heap, (0, node))
        index = [float('inf')] * n
        index[node] = 0
        count = 0

        while heap:
            distance, node = heapq.heappop(heap)
            neighbor = self.matrix[node]

            for n in neighbor:
                node_n, distance_n = n
                cur_distance = index[node] + distance_n

                if cur_distance < index[node_n]:
                    heapq.heappush(heap, (distance_n, node_n))
                    index[node_n] = cur_distance

        for i in range(len(index)):
            if index[i] <= thres:
                count += 1
        
        return count


    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        total = float('inf')
        city = 0

        for edge in edges:
            self.matrix[edge[0]].append([edge[1], edge[2] ] )
            self.matrix[edge[1]].append([edge[0], edge[2]] )

        for node in range(n):
            length = self.dfs(node, distanceThreshold, n)

            if length < total:
                total = length
                city = node
            elif length == total and node > city:
                city = node
            
        return city
       
