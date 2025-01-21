class Solution(object):
    def __init__(self):
        self.board = []
        self.m = 0
        self.n = 0
        self.word = ""

    def dfs(self, row, col, index):
        if index == len(self.word):
            return True
        
        temp = self.board[row][col]
        self.board[row][col] = "#"
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < self.m and 0 <= new_col < self.n and self.board[new_row][new_col] == self.word[index]:
                if self.dfs(new_row, new_col, index + 1):  # Recursive DFS call
                    return True
        
        self.board[row][col] = temp
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.word = word
        
        for row in range(self.m):
            for col in range(self.n):
                # Start DFS if the first character matches
                if self.board[row][col] == self.word[0]:
                    if self.dfs(row, col, 1):  # Start the search from the next character
                        return True
        
        return False
