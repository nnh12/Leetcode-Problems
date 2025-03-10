# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        if head.next is None:
            return head


        low = head
        ptr = head.next
        list = []

        if head.next.val != head.val:
            list.append(head.val)


        while (ptr != None):
            if ptr.next is None:
                if low.val != ptr.val:
                    list.append(ptr.val)
                    break

            if (ptr.next != None) and low.val != ptr.val and ptr.next.val != ptr.val:
                list.append(ptr.val)

            low = low.next
            ptr = ptr.next 

        if len(list) == 0:
            return None
        
        start = ListNode(list[0])
        ptr = start

        for i in range(1, len(list)):
            start.next = ListNode(list[i])
            start = start.next

        return ptr
