class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        queue = deque()

        for i in range(len(tickets)):
            if i == k:
                queue.append([tickets[i], 1])
            else:
                queue.append([tickets[i], 0])
        
        while queue:
            ticket, value = queue.popleft()
            ticket -= 1
            count += 1
           
            if value == 1 and ticket == 0:
                return count

            if ticket != 0:
                queue.append([ticket, value])
        
