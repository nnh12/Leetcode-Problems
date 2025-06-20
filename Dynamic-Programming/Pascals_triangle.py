class Solution(object):

    def create(self, row, col):
        if col == 0 or row == col:
            return 1
        
        return self.create(row - 1, col - 1) + self.create(row - 1, col)
        

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list = []
        for i in range(numRows):
            sub_list = []
            index = 0
            while index <= i:
                compute = self.create(i, index)
                sub_list.append(compute)
                index += 1
            list.append(sub_list)
        
        return list
        
