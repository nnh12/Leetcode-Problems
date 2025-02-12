# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        len_node = 0
        node = head
        while (node):
            len_node += 1
            node = node.next

        list = []
        node = head
        count = 0
        
        if (len_node == 1 and n >= len_node):
            return None
        
        while (node):
            if count != (len_node - n):
                list.append(node)
            count += 1
            node = node.next

        for i in range(len(list)):
            if i == 0:
                node = ListNode(list[i].val)
                copy = node
            else:
                new_node = ListNode(list[i].val)
                node.next = new_node
                node = new_node
        
        return copy
