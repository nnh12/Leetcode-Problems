class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1
        itr = 0

        while (itr <= right):
            if nums[itr] == 0:
                temp = nums[itr]
                nums[itr] = nums[left]
                nums[left] = temp

                left += 1
                itr += 1

            elif nums[itr] == 2:
                temp = nums[itr]
                nums[itr] = nums[right]
                nums[right] = temp

                right -= 1
            elif nums[itr] == 1:
                itr += 1        
        
