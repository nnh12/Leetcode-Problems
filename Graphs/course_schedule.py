class Solution(object):
    def __init__(self):
        self.matrix = {}
        self.visit = []
        self.check = True
        self.processed = []
        self.curr_visit = []
    
    def dfs(self, node):
        stack = []
        stack.append(node)

        while stack:
            top = stack.pop()
            neighbors = self.matrix.get(top)
            self.curr_visit.append(top)
            
            if neighbors:
                for n in neighbors:
                    if node == n or (n in self.curr_visit and n in self.matrix):
                        self.check = False
                        return
                        
                    if n not in self.visit and n not in self.processed:
                        stack.append(n)
                        self.visit.append(n)
            else:
                self.curr_visit = []
            

    def dfs_iterate(self):
        for key in self.matrix:
            self.curr_visit = []
            self.processed.append(key)
            self.dfs(key)

            if self.check == False:
                return False
        return True
            

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        for node in prerequisites:
            key = node[0]
            neighbor = node[1]

            if self.matrix.get(key):
                self.matrix[key].append(neighbor)
            else:
                self.matrix[key] = []
                self.matrix[key].append(neighbor)
        print(self.matrix)
        return self.dfs_iterate()
        
