class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        count = 0

        if fast is None or fast.next is None:
            return False

        while (slow != fast or count == 0):
            if fast is None or fast.next is None: 
                return False
            elif fast.next:
                fast = fast.next.next
            slow = slow.next
            count = 1
        
        return True
