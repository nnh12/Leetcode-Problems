class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = 0
        zeros = 0
        ones = 0
        low = 0 

        for high in range(len(nums)): 
            if nums[high] == 0:
                zeros += 1
            else:
                ones += 1

            while (low <= high and zeros > k):
                if nums[low] == 0:
                    zeros -= 1
                else:
                    ones -=1
                low += 1

            length = max(length, zeros + ones) 

        return length
