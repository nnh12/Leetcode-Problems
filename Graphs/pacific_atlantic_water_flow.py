class Solution(object):

    def __init__(self):
        self.m = 0
        self.n = 0
        self.heights = [[]]
        self.visit = []
        self.visit_2 = []
        self.islands = []

    def neighbors(self, row, col):
        add_set = set()

        if (row - 1 >= 0 and (self.heights[row-1][col] >= self.heights[row][col]  )):
            add_set.add((row-1, col))
        if (col - 1 >= 0 and (self.heights[row][col - 1] >= self.heights[row][col]) ):
            add_set.add((row, col-1))
        if (row + 1 < self.m and (self.heights[row+1][col] >= self.heights[row][col]) ):
            add_set.add((row+1, col))
        if (col + 1 < self.n and (self.heights[row][col+1]) >= self.heights[row][col] ):
            add_set.add((row, col+1))

        return add_set

    def dfs(self, row, col):
        stack = []
        stack.append([row, col])
        self.visit[row][col] = -1

        while stack:
            row_cur, col_cur = stack.pop()
            neighbors = self.neighbors(row_cur, col_cur)

            if neighbors:
                for n in neighbors:
                    if self.visit[n[0]][n[1]] == 0 :
                        self.visit[n[0]][n[1]] = -1
                        stack.append(n)
    
    def dfs_atlantic(self, row, col):
        stack = []
        stack.append([row, col])
        self.visit_2[row][col] = -1

        while stack:
            row_cur, col_cur = stack.pop()
            neighbors = self.neighbors(row_cur, col_cur)

            if self.visit[row_cur][col_cur] == -1:
                self.visit[row_cur][col_cur] = 0 
                self.islands.append([row_cur, col_cur])
                
            if neighbors:
                for n in neighbors:
                    if self.visit_2[n[0]][n[1]] == 0 :
                        self.visit_2[n[0]][n[1]] = -1
                        stack.append(n)

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]
        """
        self.heights = heights
        self.m = len(heights)
        self.n = len(heights[0])
        
        islands = []
        for _ in range(self.m):
            r = [0] * self.n
            r_2 = [0] * self.n
            self.visit.append(r)
            self.visit_2.append(r_2)
    
        for col in range(self.n):
            self.dfs(0, col)
        
        for row in range(self.m):
            self.dfs(row, 0)
        
        for row in range(self.m):
            self.dfs_atlantic(row, self.n - 1)
 
        for col in range(self.n):
            self.dfs_atlantic(self.m - 1, col)

        return self.islands
