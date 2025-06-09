class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        list = []

        if k == 0:
            return

        for i in nums:
            list.append(i)

        for i in range(len(nums) - k):
            nums[i + k] = list[i]
        
        for a in range(k):
            nums[a] = list[len(nums) - k + a]

