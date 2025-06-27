class Solution(object):

    def m_sort(self, nums):
        if len(nums) == 1:
            return nums
        
        mid_point = len(nums)/2
        left_list = self.m_sort(nums[:mid_point])
        right_list = self.m_sort(nums[mid_point:])
        
        return self.merge(left_list, right_list)
    
    def merge(self, left, right):
        ret = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                ret.append(left[left_index])
                left_index += 1
            elif left[left_index] > right[right_index]:
                ret.append(right[right_index])
                right_index += 1

        if left_index == len(left) and right_index < len(right):
            ret.extend(right[right_index:])
        elif left_index < len(right) and right_index == len(right):
            ret.extend(left[left_index:])

        return ret
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.m_sort(nums)
