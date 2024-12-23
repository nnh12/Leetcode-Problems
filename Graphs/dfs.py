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

    def iterate(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        for prereq in prerequisites:
            val = prereq[0]
            neighbor = prereq[1]

            if val in self.matrix:
                self.matrix[val].append(neighbor)
            else: 
                self.matrix[val] = []
                self.matrix[val].append(neighbor)

        for key in self.matrix:
            self.dfs_start(key)
            break 


        

        
