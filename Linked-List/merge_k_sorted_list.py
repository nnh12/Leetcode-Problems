# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        list = []
        for link in lists:
            while (link):
                list.append(link.val)
                link = link.next
        
        if len(list) == 0:
            return None
        
        list = sorted(list)
        head = ListNode(list[0])
        front = head
        for val in range(1, len(list)):
            new = ListNode(list[val])
            head.next = new
            head = new

        return front
        
