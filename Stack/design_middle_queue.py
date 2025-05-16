class FrontMiddleBackQueue(object):

    def __init__(self):
        self.queue = deque()

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.queue.appendleft(val)
       

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        queue = list(self.queue)
        queue.insert( len(queue) / 2, val)
        self.queue = deque(queue)
        print('push middle', self.queue)
        

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        self.queue.append(val)
        print('push back', self.queue)

    def popFront(self):
        """
        :rtype: int
        """
        if self.queue:
            val = self.queue.popleft()
            print('pop front', self.queue)
            return val
        else:
            print('pop front', self.queue)
            return -1

    def popMiddle(self):
        """
        :rtype: int
        """
        queue = list(self.queue)
        if queue:
            mid = len(queue) / 2
            val = queue[mid]
            print(queue)
            queue.pop(mid)
            
            self.queue = deque(queue)
            print('pop middle', self.queue, val)
            return val
        else:
            return -1

    def popBack(self):
        """
        :rtype: int
        """
        if self.queue:
            val = self.queue.pop()
            return val
        else:
            return - 1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
