class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    if row not in rows:
                        rows.add(row)
                    if col not in cols:
                        cols.add(col)
        
        for row in rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
        
