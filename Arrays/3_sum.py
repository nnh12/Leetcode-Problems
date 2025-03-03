class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict = {}
        list = []

        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] =[]
                dict[nums[i]].append(i)
            else:
                dict[nums[i]].append(i)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if ( -nums[i] - nums[j] in dict ):
                    dict_list = dict[-nums[i] - nums[j]]
                    for index in dict_list:
                        if index != i and index != j and sorted([nums[i], nums[j], nums[index]]) not in list:
                            list.append(sorted([nums[i], nums[j], nums[index]]))

        return list
