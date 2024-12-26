"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""


class Solution(object):
    def __init__(self):
        self.visit = []
        self.grid = []
        self.m = 0
        self.n = 0
    
    def get_neighbor(self, coordinate):
        row = coordinate[0]
        column = coordinate [1]
        list = []

        if row+1 >= 0 and row+1 < self.m -1 and self.grid[row+1][column] == '1':
                list.append([row+1, column])
        if row-1 >= 0 and row-1 < self.m and self.grid[row-1][column] == '1':
            list.append([row-1, column])
        if column+1 >= 0 and column+1 < self.n and self.grid[row][column+1] == '1':
            list.append([row, column+1])
        if column-1 >= 0 and column-1 < self.n and self.grid[row][column-1] == '1':
            list.append([row, column-1])
        return list

    def bfs(self, row, column):
        queue = deque()
        queue.append([row, column])
        
        while queue:
            top = queue.popleft()
            neighbor = self.get_neighbor(top)
            if top not in self.visit:
                self.visit.append(top)
            #print(top)

            if neighbor:
                for n in neighbor:
                    if n not in self.visit:
                        self.visit.append(n)
                        queue.append(n)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid

        islands = 0

        for row in range(self.m):
            for col in range(self.n):
                if [row, col] not in self.visit and self.grid[row][col] == '1':
                    #print([row, col])
                    #print(self.visit)
                    islands += 1
                    self.bfs(row, col)
        
        return islands
