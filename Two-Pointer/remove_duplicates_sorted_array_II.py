class Solution(object):
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        k = 0
        cur = nums[0]

        for high in range(len(nums)):
            if nums[high] == cur and k < 2:
                nums[low] = nums[high]
                low += 1
                k += 1
            elif nums[high] != cur:
                nums[low] = nums[high]
                cur = nums[high]
                low += 1
                k = 1

        print(low)
        return low
