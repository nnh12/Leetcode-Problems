class Solution(object):

    def __init__(self):
        self.matrix = {}
        self.visit = set()

    def dfs(self, node):
        queue = deque()
        queue.append(node)
        nodes = 1
        edges = 0
                
        while queue:
            top = queue.popleft()
            neighbors = self.matrix[top]
            edges += len(neighbors)
            
            for n in neighbors:
                if n not in self.visit:
                    nodes += 1
                    self.visit.add(n)
                    queue.append(n) 

        print('start node', node, 'nodes', nodes, 'edges', edges/2)
        if nodes != edges/2:
            return False
        return True

    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        count = 0
        for edge in edges:
            if edge[0] not in self.matrix:
                self.matrix[edge[0]] = set()
                self.matrix[edge[0]].add(edge[1])
            else:
                self.matrix[edge[0]].add(edge[1])
            
            if edge[1] not in self.matrix:
                self.matrix[edge[1]]= set()
                self.matrix[edge[1]].add(edge[0])
            else:
                self.matrix[edge[1]].add(edge[0])
        
        for edge in range(n):
            if edge not in self.matrix:
                print(edge)
                self.matrix[edge] = set()
                self.matrix[edge].add(edge)

        for edge in range(n):
            if edge not in self.visit and self.dfs(edge):
                count += 1

        return count
