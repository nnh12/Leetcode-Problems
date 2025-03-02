class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while (low < high):
            mid = (high + low) / 2
            
            if nums[mid] == target:
                return mid

            if (  nums[low] <= nums[mid]):
                if ( nums[low] <= target and target < nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            elif (nums[high] >= nums[mid] ):
                if (nums[high] >= target and target > nums[mid]  ):
                    low = mid + 1
                else:
                    high = mid - 1
                
        
        print('low', low, 'high', high)

        if (nums[low] == target):
            return low
        else:
            return -1
