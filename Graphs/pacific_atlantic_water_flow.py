import copy 

class Solution(object):

    def __init__(self):
        self.m = 0
        self.n = 0
        self.heights = [[]]
        self.visit = []
        self.dp = []

    def neighbors(self, row, col):
        add_set = set()

        if (row - 1 >= 0 and (self.heights[row-1][col] <= self.heights[row][col]  )):
            add_set.add((row-1, col))
        if (col - 1 >= 0 and (self.heights[row][col - 1] <= self.heights[row][col]) ):
            add_set.add((row, col-1))
        if (row + 1 < self.m and (self.heights[row+1][col] <= self.heights[row][col]) ):
            add_set.add((row+1, col))
        if (col + 1 < self.n and (self.heights[row][col+1]) <= self.heights[row][col] ):
            add_set.add((row, col+1))

        return add_set

    def dfs(self, row, col):
        stack = []
        stack.append([row, col])

        visit = []
        for _ in range(self.m):
            r = [0] * self.n
            visit.append(r)
        
        visit[row][col] = -1
        oceans = [0, 0]
        
        while stack:
            row_cur, col_cur = stack.pop()
            neighbors = self.neighbors(row_cur, col_cur)
            print([row_cur, col_cur])

            if (row_cur == 0) or (col_cur == 0):
                oceans[0] = 1
            
            if (row_cur == (self.m - 1) or col_cur == (self.n - 1)):
                oceans[1] = 1
            
            if oceans == [1, 1] or self.dp[row_cur][col_cur] == -1:
                return True

            if neighbors:
                for n in neighbors:
                    if visit[n[0]][n[1]] != -1 :
                        visit[n[0]][n[1]] = -1
                        stack.append(n)

        return False


    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]
        """
        self.heights = heights
        self.m = len(heights)
        self.n = len(heights[0])
        self.dp = copy.deepcopy(heights)
        list = []
        
        for i in range(self.m):
            for j in range(self.n-1, -1, -1):
                if self.dfs(i, j):
                    list.append([i, j])
                    self.dp[i][j] = - 1
                   
        return list

        
