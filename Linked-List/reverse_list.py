# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head
        new_node = None

        if head is None:
            return None

        while (node):
            if node.next:
                next = node.next
                node.next = new_node
                new_node = node
                node = next
            else:
                node.next = new_node
                break
                
        return node
