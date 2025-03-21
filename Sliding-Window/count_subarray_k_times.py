class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_element = max(nums)
        #print(max_element)
        low = 0
        sub_array = 0
        max_count = 0

        for high in range(len(nums)):
            if nums[high] == max_element:
                max_count += 1
            
            while (low <= high and max_count >= k):
                print('high', high, 'low', low)
                sub_array += 1
                if nums[low] == max_element:
                    max_count -= 1
                
                low += 1
        
        print(sub_array)
