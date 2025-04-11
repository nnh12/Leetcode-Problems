class Solution(object):

    def __init__(self):
        self.matrix = {}

    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        for edge in edges:
            if edge[0] not in self.matrix:
                self.matrix[edge[0]]= set()
                self.matrix[edge[0]].add(vals[edge[1]])
            else:
                self.matrix[edge[0]].add(vals[edge[1]])
            
            if edge[1] not in self.matrix:
                self.matrix[edge[1]] = set()
                self.matrix[edge[1]].add(vals[edge[0]])
            else:
                self.matrix[edge[1]].add(vals[edge[0]])

        max_sum = max(vals)
        for key in self.matrix:
            cur_sum = vals[key]
            heap = []
            heapq.heapify(heap)

            for n in self.matrix[key]:
                heapq.heappush(heap, -1*n)
            
            for _ in range(min(k, len(heap)) ):
                top = -1 * heapq.heappop(heap)
                if cur_sum + top < cur_sum:
                    break
                cur_sum += top
                
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
