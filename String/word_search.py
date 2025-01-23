class Solution(object):

    def __init__(self):
        self.board = None
        self.word = ""
        self.m = 0
        self.n = 0

    def dfs(self, row, col, index):
        if index == len(self.word) :
            return True
        
        temp = self.board[row][col]
        self.board[row][col] = "#"

        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        for n in directions:
            r, c = n
            new_r = row + r
            new_c = col + c

            print(self.board[row][col])
            if ((new_r >= 0) and (new_c >= 0) and (new_r < self.m) and (new_c < self.n) and self.board[new_r][new_c] == self.word[index]):
                if (self.dfs(new_r, new_c, index + 1)):
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

        if not board:
            return False
        else:
            for i in range((self.m)):
                for j in range((self.n)):
                    if self.board[i][j] == self.word[0]:
                        if self.dfs(i, j, 1):
                            return True
            
            return False
