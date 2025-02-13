# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        slow = head
        fast = head

        while (slow and fast):
            if not slow.next or not fast.next:
                return None
                
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        
        if (not slow or not fast):
            return None
        
        slow = head

        while (slow != fast):
            slow = slow.next
            fast = fast.next
        
        return slow
        
