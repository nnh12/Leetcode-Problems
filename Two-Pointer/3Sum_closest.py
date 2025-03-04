class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        a = 0
        print(nums)
        app = None

        while (a < len(nums) - 2):
            left = a + 1
            right = len(nums) - 1

            while (left < right):
                sum = nums[a] + nums[left] + nums[right]

                if app is None or  ( abs(target - sum) < abs(target - app)):
                    app = sum

                if (sum == target):
                    return target
                elif (sum < target):
                    left += 1
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                elif (sum > target):
                    right -= 1
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1

            a += 1
        
        return app
