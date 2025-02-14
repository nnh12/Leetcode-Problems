# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head
        len_node = 0

        while (node):
            len_node += 1
            node = node.next
        
        if len_node <= 1:
            head = None
            return head
        elif len_node == 2:
            head.next = None
            return head

        count = 0
        mid = len_node / 2
        node = head
        while (count < mid):
            curr = node
            prev = node
            node = node.next
            count += 1
        
        prev.next = node.next

        return head
