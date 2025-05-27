# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        length = 0 
        tail = None
        h = head
        list = []

        if head == None:
            return head

        while h != None:
            list.append(h.val)
            if h.next == None:
                tail = h
            h = h.next
            length += 1
        
        k = k % length
        while k > 0:
            temp  = list[len(list) - 1]
            for i in range(len(list) - 1, 0, -1):
                list[i] = list[i - 1]          

            list[0] = temp
            k -= 1
        

        head = None
        temp = None
        for i in range(len(list)):
            if i == 0:
                head = ListNode(list[i])
                temp = head
            else:
                newNode = ListNode(list[i])
                temp.next = newNode
                temp = newNode
        
        return head
