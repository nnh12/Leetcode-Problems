# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        list = []
        sum = 0
        while (head):
            list.append(head.val)
            head = head.next
        
        for i in range( (len(list)/2) ):
            i_s = (len(list) - 1 - i)
            sum = max(sum, list[i_s] + list[i])
        
        return sum
