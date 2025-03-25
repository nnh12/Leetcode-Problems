class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        matrix = {}
        n = 0

        for edge in edges:
            n = max(edge[0], edge[1], n)

            if edge[0] not in matrix:
                matrix[edge[0]] = []
                matrix[edge[0]].append(edge[1])
            else:
                matrix[edge[0]].append(edge[1])

            if edge[1] not in matrix:
                matrix[edge[1]] = []
                matrix[edge[1]].append(edge[0])
            else:
                matrix[edge[1]].append(edge[0])               

        for node in matrix:
            if len(matrix[node]) == n - 1:
                return node
        
        return 0
