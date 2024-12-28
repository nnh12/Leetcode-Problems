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
        self.queue = deque()
        self.count = 0
        self.m = 0
        self.n = 0
    
    def get_neighbor(self, coordinate, check):
        row = coordinate[0]
        column = coordinate[1]
        list = []

        if row+1 >= 0 and row+1 < self.m and self.grid[row+1][column] == check:
            list.append([row+1, column])
        elif row+1 >= 0 and row+1 < self.m and self.grid[row+1][column] != check:
            if [row+1, column] not in self.visit and [row+1, column] not in self.queue:
                self.queue.append([row+1, column])

        if row-1 >= 0 and row-1 < self.m and self.grid[row-1][column] == check:
            list.append([row-1, column])
        elif row-1 >= 0 and row-1 < self.m and self.grid[row-1][column] != check:
            if [row-1, column] not in self.visit and [row-1, column] not in self.queue:
                self.queue.append([row-1, column])

        if column+1 >= 0 and column+1 < self.n and self.grid[row][column+1] == check:
            list.append([row, column+1])
        elif column+1 >= 0 and column+1 < self.n and self.grid[row][column+1] != check:
            if [row, column+1] not in self.visit and [row, column+1] not in self.queue:
                self.queue.append([row, column+1])

        if column-1 >= 0 and column-1 < self.n and self.grid[row][column-1] == check:
            list.append([row, column-1])
        elif column-1 >= 0 and column-1 < self.n and self.grid[row][column-1] != check:
            if [row, column-1] not in self.visit and [row, column-1] not in self.queue:
                self.queue.append([row, column-1])

        return list

    def bfs(self, node):
        queue = deque()
        queue.append(node)

        while queue:
            top = queue.popleft()
            neighbors = self.get_neighbor(top, self.grid[top[0]][top[1]] )
            #print(top)

            if top not in self.visit:
                self.visit.append(top)

            for n in neighbors:
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
        self.queue.append([0,0])
        
        while self.queue:
            top = self.queue.popleft()
            if top not in self.visit:
                if self.grid[top[0]][top[1]] == '1':
                    islands += 1
                self.bfs(top)
            print(self.queue)

        return islands
