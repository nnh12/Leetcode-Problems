class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]
        count = 0
        while (count == 0 or slow != fast):
            print(slow, count)
            count = 1
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = nums[0]
        while (slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        print(slow, fast)
        return slow
                
        return nums[slow]
