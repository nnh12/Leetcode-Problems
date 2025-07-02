class Solution(object):

    def search_row(self, low, high, matrix, target):
        low_list = matrix[low]
        high_list = matrix[high]

        start_low = low_list[0]
        end_low = low_list[-1]
        start_high = high_list[0]
        end_high = high_list[-1]

        if low > high:
            return None
        
        if target >= start_low and target <= end_low:
            return low_list
        elif target >= start_high and target <= end_high:
            return high_list
        elif target > end_low and target < start_high:
            return self.search_row(low + 1, high - 1, matrix, target)

    def search_num(self, low, high, list, target):
        if low >= high:
            return False

        mid = (high + low) / 2

        if list[mid] == target:
            return True
        elif list[mid] > target:
            return self.search_num(low, high - 1, list, target)
        elif list[mid] < target:
            return self.search_num(low + 1, high, list, target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if len(matrix) == 1:
            return self.search_num(0, len(matrix[0]), matrix[0], target    )

        row = self.search_row(0, len(matrix) - 1, matrix, target)
        if row is None:
            return False

        return self.search_num(0, len(row), row, target)
