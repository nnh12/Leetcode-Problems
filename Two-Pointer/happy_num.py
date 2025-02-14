import math

class Solution(object):

    def split_num(self, n):
        nums = []
        while (n >= 1):
            new_num = n % 10
            n /= 10
            nums.append(new_num)
        
        new_num = 0
        for n in nums:
            new_num += n ** 2
        
        return new_num
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n
        count = 0

        while (count == 0 or (fast != slow)):
            if fast == 1:
                return True            
            count = 1
            fast = self.split_num(self.split_num(fast))
            slow = self.split_num(slow)
        
        if fast == 1:
            return True
        else:
            return False
        

