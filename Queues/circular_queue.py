class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.head = None
        self.length = k
        self.cur_length = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.head == None:
            head = Node(value)
            self.head = head
            self.cur_length += 1
            return True
        else:
            if self.cur_length >= self.length:
                return False

            ptr = self.head
            
            while ptr != None:
                prev = ptr
                ptr = ptr.next
                
            self.cur_length += 1
            newNode = Node(value)
            prev.next = newNode
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.head is None:
            return False
        else:
            head = self.head
            if head.next is None:
                self.head = None
            else:
                self.head = self.head.next

            self.cur_length -= 1
            return True

    def Front(self):
        """
        :rtype: int
        """
        if self.head is None:
            return -1
        else:
            val = self.head.val
            return val


    def Rear(self):
        """
        :rtype: int
        """
        if self.head is None:
            return -1
        else:
            ptr = self.head 
            while ptr.next != None:
                ptr = ptr.next
            
            return ptr.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.head is None:
            return True
        else:
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.cur_length == self.length:
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
