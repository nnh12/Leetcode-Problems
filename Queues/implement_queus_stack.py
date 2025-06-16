class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.dump = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.dump:
            while self.stack:
                top = self.stack.pop()
                self.dump.append(top)
            
            top = self.dump.pop()
            return top
       
        top = self.dump.pop()
        return top
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.dump:
            while self.stack:
                top = self.stack.pop()
                self.dump.append(top)
            
        top = self.dump[-1]
        return top
        
        

    def empty(self):
        """
        :rtype: bool
        """
        print(self.stack, self.dump)
        if not self.stack and not self.dump:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
