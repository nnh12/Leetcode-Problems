class Solution(object):

    def __init__(self):
        self.grid = []
        self.m = 0
        self.n = 0
    
    def neighbors(self, row, col):
        list = []

        if (row + 1 < self.m and self.grid[row+1][col] == 1):
            list.append([row + 1, col])
        if (col + 1 < self.n and self.grid[row][col + 1] == 1):
            list.append([row, col + 1])
        if (row - 1 >= 0 and self.grid[row-1][col] == 1):
            list.append([row - 1, col])
        if (col - 1 >= 0 and self.grid[row][col - 1] == 1):
            list.append([row, col - 1])

        return list

    def bfs(self, row, col):
        queue = deque()
        queue.append([row, col])
        count = 0

        while queue:
            top = queue.popleft()
            neighbors = self.neighbors(top[0], top[1])
            self.grid[top[0]][top[1]] = 0
            count += 1

            if neighbors:
                for n in neighbors:
                    if (self.grid[n[0]][n[1]] == 1):
                        self.grid[n[0]][n[1]] = 0
                        queue.append(n)
        
        return count

            
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        max = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    area = self.bfs(i, j)
                    if (area > max):
                        max = area

        return max
