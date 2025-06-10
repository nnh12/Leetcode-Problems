class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                count += 1
                for a in range(i, i + 3):
                    if nums[a] == 0:
                        nums[a] = 1
                    else:
                        nums[a] = 0
                
        if 0 not in nums:
            return count
        else:
            return -1
