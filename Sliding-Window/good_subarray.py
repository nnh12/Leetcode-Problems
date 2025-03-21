class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict = {}
        length = 0
        low = 0
        common = deque()

        for high in range(len(nums)):
            if nums[high] not in dict:
                dict[nums[high]] = 1
            else:
                dict[nums[high]] += 1
            
            while (common and common[-1][0] < dict[nums[high]] ):
                common.pop()

            common.append( [dict[nums[high]], nums[high] ])

            while (low <= high and common and common[0][0] > k):
                if common[0][1] == nums[low]:
                    common.popleft()
                
                dict[nums[low]] -= 1
                low += 1
            
            length = max(length, high - low + 1)

        return length
