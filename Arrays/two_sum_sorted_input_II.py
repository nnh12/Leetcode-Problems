class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
            
        for i in range(len(numbers)):
            if target - numbers[i] in dict:
                list = sorted([i + 1, dict[target - numbers[i]] + 1])
                return list
            else:
                dict[numbers[i]] = i
