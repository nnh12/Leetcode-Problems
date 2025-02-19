# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        list = []

        while (list1):
            list.append(list1.val)
            list1 = list1.next
        
        while (list2):
            list.append(list2.val)
            list2 = list2.next
        
        list = sorted(list)

        new = None
        start = None

        for i in range(len(list)):
            if i == 0:
                new = ListNode(list[i])
                start = new
            else:
                new.next = ListNode(list[i])
                new = new.next
            
        return start
