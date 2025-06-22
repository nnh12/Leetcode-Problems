class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        cache = {}
        cache[0] = 0
        cache[1] = 1
        cache[2] = 2

        def helper(num, cache):
            if num in cache:
                return cache[num]
            else:
                cache[num] = helper(num - 1, cache) + helper(num - 2, cache)
            
            res = helper(num - 1, cache) + helper(num - 2, cache)
            return res
        
        return helper(n, cache)
