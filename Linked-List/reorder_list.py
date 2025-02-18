# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse(self, head):
        
        node = head
        new_node = None

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

    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        count = 0
        prev = None

        while (fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev is None:
            return
        
        rear = self.reverse(slow)
        prev.next = None
                
        while (head or rear):
            if head.next is None:
                head.next = rear
                break

            next = head.next
            next_rear = rear.next

            head.next = rear
            rear.next = next
            rear = next_rear
            head = next
