class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        dict = {}
        list = [-1] * len(nums1)

        for i in range(len(nums2)):
            current_element = nums2[i]

            while stack and nums2[stack[-1]] < current_element:
                index = stack.pop()
                dict[nums2[index]] = current_element
            stack.append(i)
        
        for i in range(len(nums1)):
            if nums1[i] in dict:
                list[i] = dict[nums1[i]]
        
        return list
