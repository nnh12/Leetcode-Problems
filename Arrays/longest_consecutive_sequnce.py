class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        start_dict = {}
        max_len = 1

        if not nums:
            return 0

        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        
        for key in num_dict:
            if num_dict.get(key - 1) is None and num_dict.get(key + 1):
                start_dict[key] = 1           
        
        for key in start_dict:
            count = 0
            while (num_dict.get(key)):
                print(key)
                key += 1
                count += 1

            max_len = max(count, max_len)

        return max_len
