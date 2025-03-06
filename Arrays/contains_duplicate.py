class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = set()

        for i in nums:
            if i not in dict:
                dict.add(i)
            else:
                return True
        
        return False
