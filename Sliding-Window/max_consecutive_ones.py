class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = 0
        zeros = 0
        ones = 0
        low = 0 

        for high in range(len(nums)): 
            
            if nums[high] == 0:
                zeros += 1
            else:
                ones += 1

            if zeros > k and k != 0:
                print('here')
                length = max(length, high - low)
                while (low < high and zeros > k):
                    if nums[low] == 0:
                        zeros -= 1
                    else:
                        ones -= 1
                    low += 1
            else:
                if k == 0 and nums[high] == 0 or (k == 0 and high == len(nums) - 1):
                    print(high, ones)
                    length = max(length, ones)
                    ones = 0
                elif k != 0:
                    length = max(length, ones + zeros)        

        return length
