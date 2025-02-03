class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        window = nums[0]
        right = 0
        win_len = len(nums) + 1

        for left in range(len(nums)):
            
            while (right < len(nums)):
                if (window >= target or right == len(nums) - 1):
                    break
                right += 1
                window += nums[right]
                
            if window >= target:
                win_len = min(win_len, right - left + 1)
                window -= nums[left]
        
        if win_len == len(nums) + 1:
            return 0
        else:
            return win_len


            
            

        
