class Solution(object):
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = nums[0]
        count = 1
        subtract = 0
        length = len(nums)

        for i in range(1, length):
            if i >=  length:
                break
            if nums[i] == cur and count < 2:
                count += 1
            elif nums[i] == cur and count == 2:
                index = i + 1
                original = i
                length -= 1

                print('heeq')
                while (index < len(nums) and nums[index] == cur ):
                    index += 1
                    length -= 1
                    print(length)                   

                print(original, index)
                for a in range(index , len(nums)):
                    nums[original] = nums[a]
                    original += 1

                count = 1
                cur = nums[i]
            elif nums[i] != cur:
                count = 1
                cur = nums[i]
            
            print('here', i, count, nums)
        
        print(length)
        return length
