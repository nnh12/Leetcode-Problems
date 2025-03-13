class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = []
                dict[nums[i]].append(i)
            else:
                dict[nums[i]].append(i)
        
        for i in range(len(nums)):
            for index in dict[nums[i]]:
                if index != i and abs(index - i) <= k:
                    return True
        
        return False
