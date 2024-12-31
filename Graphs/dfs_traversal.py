# Depth First Search Implementation

# node - > neighbors
# 1 -> 0, 1, 4, 5
# 2 -> 1, 2

class Solution(object):
    def __init__(self):
        self.matrix = {}
        self.course = True
       
    def dfs_start(self, node):
        stack = []
        visit = []
        stack.append(node)

        while stack:
            top = stack.pop()
            print(top)
            neighbors = self.matrix.get(top)
            if neighbors:
                for n in neighbors:
                    if n not in visit:
                        visit.append(n)
                        stack.append(n)

    def build_adj_matrix(self, val, list_node):
        """
        :type val: int
        :type list_node: List[List[int]]
        :rtype: bool
        """

        for node in list_node:
            val = node[0]
            neighbor = node[1]

            if val in self.matrix:
                self.matrix[val].append(neighbor)
            else: 
                self.matrix[val] = []
                self.matrix[val].append(neighbor)
                
        # Itereate through adj matrix using dfs from node in list_node              
        self.dfs_start(self.matrix[list_node[0][0]])
