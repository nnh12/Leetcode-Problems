class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        max_prod = nums[0]

        for i in range(1, len(nums)):
            temp_max = cur_max
            temp_min = cur_min

            cur_max = max(nums[i], temp_max * nums[i], temp_min * nums[i]     ) 
            cur_min = min(nums[i], temp_max * nums[i], temp_min * nums[i] )

            max_prod = max(cur_max, max_prod)

        
        return max_prod            
