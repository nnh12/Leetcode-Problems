class Solution(object):

    def helper(self, n, k, rootVal):
        if n == 1:
            return rootVal
        
        mid_num_nodes = ( 2**(n-1)) / 2
        if k > mid_num_nodes:
            if rootVal == 0:
                rootVal = 1
            else:
                rootVal =0
            return self.helper(n-1, k-mid_num_nodes, rootVal)
        else:
            if rootVal ==0:
                rootVal =0
            else:
                rootVal = 1
            return self.helper(n-1,k, rootVal)
        
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return self.helper(n, k, 0)
