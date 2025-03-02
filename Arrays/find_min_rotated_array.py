class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1):
            return nums[0]

        low = 0
        high = len(nums) - 1
        length = len(nums) - 1
        org_mid = (high + low) / 2
        count = 0

        while (low < high):
            mid = (high + low) / 2 

            print('mid', mid)
            if (nums[mid]  > nums[high] ):
                low = mid + 1
                print('low', low)
            else:
                high = mid 
                print('high', high)

        return nums[low]
