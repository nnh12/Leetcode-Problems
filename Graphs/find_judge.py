class Solution(object):
    def __init__(self):
        self.matrix = {}
        self.visit = []
        self.no_neighbor = []

    def dfs(self, node):
        stack =[]
        stack.append(node)

        while stack:
            top = stack.pop()
            neighbor = self.matrix.get(top)
            if top not in self.visit:
                self.visit.append(top)

            if neighbor:
                for n in neighbor:
                    if n not in self.visit:
                        if n not in self.matrix:
                            self.no_neighbor.append(n)
                        self.visit.append(n)
                        stack.append(n)

    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust and n == 1:
            return n

        for nodes in trust:
            node = nodes[0]
            neighbor = nodes[1]
            if self.matrix.get(node):
                self.matrix[node].append(neighbor)
            else:
                self.matrix[node] = []
                self.matrix[node].append(neighbor)
        
        for key in self.matrix:
            self.dfs(key)
        
        print(self.matrix)
        print(self.no_neighbor)

        for judge in self.no_neighbor:
            print(judge)
            if judge in self.matrix:
                self.no_neighbor.remove(judge)
            else:
                for node in self.visit:
                    print(node)
                    if judge in self.no_neighbor:
                        self.no_neighbor.remove(judge)
                    
                    
                    
                
        if len(self.no_neighbor) == 1:
            return self.no_neighbor[0]
        else:
            return -1
            
        
