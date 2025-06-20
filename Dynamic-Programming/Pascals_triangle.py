class Solution(object):
     

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list = []
        for row in range(numRows):
            sub_list = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    sub_list.append(1)
                else:
                    cur = list[row-1][col-1] + list[row-1][col]
                    sub_list.append(cur)
            list.append(sub_list) 
        
        return list
