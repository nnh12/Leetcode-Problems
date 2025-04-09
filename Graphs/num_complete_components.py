class Solution(object):

    def __init__(self):
        self.matrix = {}
        self.visit = set()

    def dfs(self, node):
        queue = deque()
        queue.append(node)
        self.visit.add(node)
        nodes = 0
        edges = 0
                
        while queue:
            top = queue.popleft()
            neighbors = self.matrix[top]
            edges += len(neighbors)
            nodes += 1
            print('top', top, len(neighbors))

            for n in neighbors:
                if n not in self.visit:
                    self.visit.add(n)
                    queue.append(n) 

       
        hi = nodes * (nodes - 1) / 2
        print('start node', node, 'nodes', nodes, 'edges', edges/2, 'hi', hi)

        if edges/2 == hi:
            return True
        return False

    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        sum = 0
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
                sum += 1

        return sum
