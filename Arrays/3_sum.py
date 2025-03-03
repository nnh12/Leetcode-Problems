class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list = []
        a = 0
        nums = sorted(nums)

        while (nums[a] <= 0 and a < len(nums) - 2):
            left = a + 1
            right = len(nums) - 1

            if a > 0 and nums[a] == nums[a - 1]:
                a += 1
                continue

            while (left < right):
                sum = nums[a] + nums[left] + nums[right]

                if sum == 0:
                    list.append([nums[a], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1
                elif (sum < 0):
                    left += 1
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                elif (sum > 0):
                    right -= 1
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1
            
            a += 1

        return list
