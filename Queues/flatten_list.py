# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = deque()
        self.get_level(nestedList)

    def get_level(self, nestedList):
        list_l = []
        for nest in nestedList:
            self.queue.append(nest)


    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.queue:
            top = self.queue[0]
            if top.isInteger():
                return True
            else:
                self.queue.popleft()
                for n in reversed(top.getList()):
                    self.queue.appendleft(n)
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
