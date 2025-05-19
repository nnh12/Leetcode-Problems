class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.length = k
        self.count = 0
        self.head = None
        self.tail = None

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count + 1 > self.length:
            return False

        if self.head == None and self.tail == None:
            newNode = Node(value)
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(value)
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode

        self.count += 1
        return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count + 1 > self.length:
            return False

        if self.head == None and self.tail == None:
            newNode = Node(value)
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(value)
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

        self.count += 1
        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.head == None and self.tail == None:
            return False
        else:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
        
        self.count -= 1
        return True


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.head == None and self.tail == None:
            return False
        else:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
        
        self.count -= 1
        return True 

    def getFront(self):
        """
        :rtype: int
        """
        if self.head == None:
            return -1
        else:
            return self.head.val        

    def getRear(self):
        """
        :rtype: int
        """
        if self.tail == None:
            return -1
        else:
            return self.tail.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.head == None and self.tail == None:
            return True
        else:
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.count == self.length:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
