class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        max_num = sum
        for i in range(1, len(nums)):
            sum = max(sum + nums[i], nums[i])

            max_num = max(max_num, sum)
        
        return max_num
