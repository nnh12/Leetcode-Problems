# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse(self, node):
        prev = None

        while (node):
            if node.next:
                next = node.next
                node.next = prev
                prev = node
                node = next
            else:
                node.next = prev
                break
            
        return node


    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        count = 0 

        while (count == 0 or (fast and fast.next)):
            slow = slow.next
            fast = fast.next.next
            count = 1
        
        print(slow.val)

