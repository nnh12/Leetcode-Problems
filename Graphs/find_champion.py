class Solution(object):

    def __init__(self):
        self.node_list = set()
        self.matrix = {}
        self.visit = set()

    def dfs(self, node):
        queue = deque()
        queue.append(node)

        while queue:
            top = queue.popleft()
            if top in self.matrix:
                neighbors = self.matrix[top]
                for n in neighbors:
                    if n in self.node_list:
                        self.node_list.remove(n)
                    if n not in self.visit:
                        self.visit.add(n)
                        queue.append(n)



    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges and n == 1:
            return 0

        matrix = {}
        for edge in edges:
            if edge[0] not in self.matrix:
                self.node_list.add(edge[0])
                self.node_list.add(edge[1])
                self.matrix[edge[0]] = []
                self.matrix[edge[0]].append(edge[1])
            else:
                self.node_list.add(edge[1])
                self.matrix[edge[0]].append(edge[1])
        
        if len(self.node_list) != n:
            return -1

        for edge in edges:
            self.dfs(edge[0])
        
        if len(self.node_list) != 1:
            return -1
        else:
            return next(iter(self.node_list))
