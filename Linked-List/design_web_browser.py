class Node(object):
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head = Node(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        newNode = Node(url)
        prev = self.head
        self.head.next = newNode
        self.head = self.head.next
        self.head.prev = prev
        self.head.next = None

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while (self.head.prev != None and steps > 0):
            self.head = self.head.prev
            steps -= 1
        
        return self.head.url
        
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while (self.head.next != None and steps > 0):
            self.head = self.head.next
            steps -= 1

        return self.head.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
