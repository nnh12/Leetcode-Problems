class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        i, j = edges[0][0], edges[0][1]
        if i in edges[1]:
            return i
        return j
