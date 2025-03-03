class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list = []
        a = 0
        nums = sorted(nums)

        while (a < len(nums) - 2 ):
            left = a + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[a] + nums[right]
                print(a, left, right)

                if sum == 0:
                    sublist = sorted([  nums[left] , nums[a], nums[right]  ])
                    if sublist not in list:
                        list.append(sublist)
                    left += 1
                    right -= 1
                    
                elif (sum < 0):
                    left += 1
                elif (sum > 0):
                    right -= 1
            
            a += 1

        return list
