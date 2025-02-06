class Solution(object):

    def __init__(self):
        self.m = 0
        self.n = 0
        self.heights = [[]]
        self.copy_heights = [[]]

    def neighbors(self, row, col):
        list = []
        print('compare point to', row, col)

        if row-1 >=0 and (self.heights[row-1][col] <= self.heights[row][col]):
            list.append([row-1, col])
        if col -1 >= 0 and (self.heights[row][col-1] <= self.heights[row][col]):
            list.append([row, col-1])
        if row+ 1 < self.m and (self.heights[row+1][col] <= self.heights[row][col]):
            list.append([row + 1, col])
        if col + 1 < self.n and (self.heights[row][col+1] <= self.heights[row][col]):
            print('here')
            list.append([row, col + 1])

        print(row, col, list)
        return list

    def dfs(self, row_init, col_init ):
        stack = []
        stack.append([row_init, col_init])
        oceans = [0, 0]
        copy_heights = self.copy_heights
        
        while stack:
            top = stack.pop()
            row, col = top  
            print([row, col])

            neighbors = self.neighbors(row, col)

            if (row == 0) or (col == 0):
                print(row, col)
                oceans[0] = 1
            
            if (row == self.m -1) or (col == self.n-1):
                print(row, col)
                oceans[1] = 1
            
            if oceans == [1, 1]:
                return [1, 1]

            for n in neighbors:
                row_n, col_n = n
                if self.copy_heights[row_n][col_n] != "*":
                    self.copy_heights[row_n][col_n] = "*"
                    stack.append([row_n, col_n])

        self.copy_heights = copy_heights
        return oceans

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]
        """
        self.heights = heights
        self.m = len(heights)
        self.n = len(heights[0])
        self.copy_heights = heights
        list = []

        if heights == [[1]]:
            return []
        
        print(self.dfs(2, 2))

#        for i in range(self.m):
#            for j in range(self.n):
#                if self.dfs(i, j) == [1, 1]:
#                    list.append([i, j])

        print(list)
        return list

        
