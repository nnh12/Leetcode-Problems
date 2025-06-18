# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def helper(self, prev, head, start):
        if head == None or head.next == None:
            return start
        
        if prev == None:
            swap = head.next
            head.next = head.next.next
            swap.next = head
            head = swap
            prev = head.next
            start = head
        else:
            swap = head.next
            head.next = head.next.next
            swap.next = head
            head = swap
            prev.next = head
            prev = head.next
            
        return self.helper(prev, head.next.next, start)

    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        h = self.helper(None, head, head)
        return h
