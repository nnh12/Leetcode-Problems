import math
class Solution(object):

    def help(self, n,  k, count):
        total = 2**(n -1)
        half_point = total/2

        if n == 1:
            return count
        
        if k > half_point:
            return self.help(n -1, k - half_point, count + 1)
        else:
            return self.help(n -1, k, count)


    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        N = math.ceil(math.log(k, 2)) + 1
        increment = self.help(N, k, 0)
        return chr(ord('a') + increment)
