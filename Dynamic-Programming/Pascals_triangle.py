class Solution(object):

    def get_number(self, row, col, sub_list, list):
        if col == row:
            sub_list.append(1)
            return sub_list
        else:   
            if col == 0:
                cur = 1
            else:
                cur = list[row-1][col-1] + list[row-1][col]
            sub_list.append(cur)
            if self.get_number(row, col + 1, sub_list, list):
                return sub_list

    def helper(self, row, rowIndex, list):
        if row == rowIndex:
            return list
        
        sub_list = self.get_number(row, 0, [], list)
        
        list.append(sub_list)
        if self.helper(row + 1, rowIndex, list):
            return list

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = self.helper(0, rowIndex + 1, [])
        return res[rowIndex]
        
