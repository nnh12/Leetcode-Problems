class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while (low <= high):
            mid = (high + low) / 2 

            print(mid)
            if (mid == 0):
                return nums[0]
            
            if (mid == len(nums) - 1):
                return nums[len(nums) - 1]
            
            if (nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]):
                return nums[mid + 1]
            
            if (nums[mid] < nums[mid + 1] and nums[mid] > nums[mid - 1]):
                high = mid - 1
                print('here', high)
