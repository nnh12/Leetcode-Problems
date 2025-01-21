class Solution(object):
    def __init__(self):
        self.matrix = []
        self.visited = []

    def build_matrix(self, isConnected):
        for city in range(len(isConnected)):
            self.matrix.append([])
            for conn in range(len(isConnected[0])):
                if conn != city and isConnected[city][conn] == 1:
                    self.matrix[city].append(conn)

    def dfs(self, city):
        self.visited.append(city)
        neighbors = self.matrix[city]
        print(city)

        for n in neighbors:
            if n not in self.visited:
                self.visited.append(n)
                self.dfs(n)

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        self.build_matrix(isConnected)
        print(self.matrix)
        count = 0

        for city in range(len(isConnected)):
            if city not in self.visited:
                self.dfs(city)
                count += 1

        return count
        
