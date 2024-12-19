# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.

# Input: nums = [1,3,5,6], target = 5
# Output: 2


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
            
        low = 0
        high = len(nums) - 1
        mid = 0

        while (low <= high):
            mid = (low + high)/ 2
            if (nums[mid] > target):
                high = mid - 1
            elif (nums[mid] < target):
                low = mid + 1
            else:
                return mid

        return low
