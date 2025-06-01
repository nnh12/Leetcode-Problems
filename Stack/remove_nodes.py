# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list = []
        stack = []

        while head != None:
            list.append(head.val)
            head = head.next
        
        for i in range(len(list)):
            cur = list[i]

            while stack and stack[-1] < cur:
                stack.pop()
            
            stack.append(cur)
        
        if stack:
            head = ListNode(stack[0])
            h = head

            for i in range(1, len(stack)):
                h.next = ListNode(stack[i])
                h = h.next
            return head
        else:
            return None
          
