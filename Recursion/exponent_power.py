class Solution(object):

    def itereate(self, x, n, total):
        if n == 1:
            return x
        
        if n % 2 != 0:
            total = self.itereate(x, n- 1, total)

            return x*total
        else:
            total = self.itereate(x, n/2, total) 
            return total * total
            

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
            
        total = self.itereate(x, abs(n), 1)
        if n < 0:
            return 1/total
        return total
