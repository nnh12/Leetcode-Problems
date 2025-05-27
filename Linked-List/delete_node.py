# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        while node != None:
            if node.next != None:
                next_val = node.next.val
                node.val = next_val
            else:
                prev.next = None
                break

            prev = node
            node = node.next
