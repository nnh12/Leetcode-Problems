# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        list_b = []
        list_a = []

        ptr = head
        while (ptr != None):
            if ptr.val < x:
                list_b.append(ptr.val)
            else:
                list_a.append(ptr.val)
            ptr = ptr.next
        
        for i in range(len(list_a)):
            list_b.append(list_a[i])

        head = ListNode(list_b[0])
        ptr = head

        for i in range(1, len(list_b)):
            head.next = ListNode(list_b[i])
            head = head.next
        
        return ptr
