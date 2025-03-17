class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        count = 0
        max_sub = 0
        
        for high in nums:
            if high not in dict:
                dict[high] = 1
            else:
                dict[high] += 1
        
        print(dict)
        for i in dict:
            if i - 1 in dict:
                print(i, i - 1, dict[i], dict[i - 1])
                cur = dict[i] + dict[i - 1]
                max_sub = max(max_sub, cur)
        
        return max_sub
