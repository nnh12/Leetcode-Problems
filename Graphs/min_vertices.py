class Solution(object):


    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        matrix = defaultdict(set)
        list = []
        no_list = set()

        for edge in edges:
            matrix[edge[0]].add(edge[1])
        
        for key in matrix:
            for ne in matrix[key]:
                no_list.add(ne)
        
        for node in range(n):
            if node not in no_list:
                list.append(node)
        
        return list
