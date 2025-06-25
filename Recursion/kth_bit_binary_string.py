class Solution(object):

    def helper(self, n, k, flip):
        if n == 2:
            if flip:
                string = "001"
            else:
                string = "011"
            
            return string[k-1]
            
        
        total_num = 2**(n) - 2
        half_point = (total_num/2) + 1
        
        if k == half_point:
            if flip:
                return "0"
            return "1"
        
        if k < half_point:
            return self.helper(n-1, k, 0)
        else:
            return self.helper(n-1, k - half_point, 1)

    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k == 1:
            return "0"
        return self.helper(n, k ,0)
