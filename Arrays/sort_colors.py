class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0

        for i in nums:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1
            elif i == 2:
                twos += 1
        

        for i in range(len(nums)):
            if zeros > 0:
                nums[i] = 0
                zeros -=1
            elif ones > 0:
                nums[i] = 1
                ones -= 1
            elif twos > 0:
                nums[i] = 2
                twos -= 1
        
        
