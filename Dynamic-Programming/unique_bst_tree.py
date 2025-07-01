class Solution(object):

    def iterate(self, index, n, cache):
        if index > n:
            return cache[n]
        
        right_len = n - index
        left_len = index - 1

        if left_len == 0 and n not in cache:
            if right_len in cache:
                cache[n] = cache[right_len]
        elif right_len == 0 and n in cache:
            if left_len in cache:
                cache[n] += cache[left_len]
            
            return cache
        else:
            cache[n] += (cache[left_len] * cache[right_len])
            
        return self.iterate(index + 1, n, cache)

    def helper(self, index, n, cache):
        right_len = n - index
        
        if right_len in cache:
            return self.iterate(index, n, cache)
            
        right_total = self.helper(index, n - 1, cache) 
        return self.iterate(index, n , cache)
        

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        cache[1] = 1
        cache[2] = 2
        cache[3] = 5
        if n in cache:
            return cache[n]
        cache = self.helper(1, n, cache)
        return cache[n]
