class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        queue = deque()
        count = 1
        for i in range(1, n + 1):
            queue.append(i)
        
        while len(queue) != 1:
            
            for i in range(k - 1):
                top = queue.popleft()
                queue.append(top)

            top = queue.popleft()
        
        return queue.pop()
