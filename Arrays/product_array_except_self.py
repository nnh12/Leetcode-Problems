class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if i == 1:
                prefix[i] = nums[i-1]
            else:
                print(nums[i-1], prefix[i-2])
                prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if i == len(nums) - 2:
                suffix[i] = nums[i + 1]
            else:
                suffix[i] = nums[i + 1] * suffix[i + 1]
        
        for i in range(len(nums)):
            dp[i] = prefix[i] * suffix[i]

        print(dp)
        return dp
        
