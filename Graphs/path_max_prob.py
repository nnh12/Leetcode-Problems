class Solution(object):
    
    def __init__(self):
        self.matrix = defaultdict(list)


    def create_path(self, node, n):
        heap = []
        heapq.heapify(heap)
        index = [float('-inf')] *n
        index[node] = 0
        heapq.heappush(heap, (1, node))
        
        while heap:
            distance, top = heapq.heappop(heap)
            neighbors = self.matrix[top]

            for n in neighbors:
                distance_n, node_n = n
                cur_distance = abs(distance_n * distance)

                if cur_distance > index[node_n]:
                    index[node_n] = cur_distance
                    heapq.heappush(heap, (-1*cur_distance, node_n )      )
                
        return index 


    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        print(succProb)
        index = 0
        for edge in edges:
            self.matrix[edge[0]].append([succProb[index], edge[1] ])
            self.matrix[edge[1]].append([succProb[index], edge[0]])
            index += 1

        index = self.create_path(start_node, n) 

        if index[end_node] == float('-inf'):
            return 0
        else:
            return index[end_node] 
