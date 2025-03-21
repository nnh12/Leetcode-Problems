class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        zeros = 0
        low = 0
        length = 0

        for high in range(len(nums)):
            if nums[high] == 1:
                ones += 1
            else:
                zeros += 1
            
            while (low <= high and zeros > 1):
                if nums[low] == 1:
                    ones -= 1
                else:
                    zeros -= 1
                
                low += 1
            
            length = max(length, zeros + ones - 1)

        return length      
