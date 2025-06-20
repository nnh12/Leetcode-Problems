class Solution(object):
    
    def calculate(self, n, cache):
        if n in cache:
            return cache[n]
        
        cache[n] = self.calculate(n-3, cache) + self.calculate(n-2, cache) + self.calculate(n -1, cache)
        return cache[n]


    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        cache[0] = 0
        cache[1] = 1
        cache[2] = 1
        num =  self.calculate(n, cache)
        return num
