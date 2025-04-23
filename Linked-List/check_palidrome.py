# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def check(self, node, start):
        if node == None:
            return True
        
        state = self.check(node.next, start )
        if not state:
            return False

        if node.val != start[0].val:
            return False

        start[0] = start[0].next
        return True

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        state = self.check(head, [head])
        return state
