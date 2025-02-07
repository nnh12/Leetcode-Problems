import copy 

class Solution(object):

    def __init__(self):
        self.m = 0
        self.n = 0
        self.heights = [[]]
        self.visit = []

    def neighbors(self, row, col):
        list = []

        if (row - 1 >= 0 and (self.heights[row-1][col] <= self.heights[row][col]  )):
            print(self.heights[row-1][col], 'is less than', self.heights[row][col])
            list.append([row-1, col])
        if (col - 1 >= 0 and (self.heights[row][col - 1] <= self.heights[row][col]) ):
            print(self.heights[row][col - 1], 'is less than', self.heights[row][col])
            list.append([row, col-1])
        if (row + 1 < self.m and (self.heights[row+1][col] <= self.heights[row][col]) ):
            print(self.heights[row+1][col], 'is less than', self.heights[row][col])
            list.append([row+1, col])
        if (col + 1 < self.n and (self.heights[row][col+1]) <= self.heights[row][col] ):
            print(self.heights[row][col + 1], 'is less than', self.heights[row][col])
            list.append([row, col+1])

        return list

    def dfs(self, row, col):
        stack = []
        stack.append([row, col])
        visit = copy.deepcopy(self.heights)
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
            
            if oceans == [1, 1]:
                print('yes')
                return True

            if neighbors:
                for n in neighbors:
                    if visit[n[0]][n[1]] != -1 :
                        print(n, 'not in ', self.visit)
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
        list = []
        
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(i, j):
                    list.append([i, j])
        print(list)
        return list

        
