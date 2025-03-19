class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_q = deque()
        min_q = deque()
        length = 0
        low = 0

        for high in range(len(nums)):           
            while (max_q and max_q[-1] < nums[high] ):
                max_q.pop()
            
            while (min_q and min_q[-1] > nums[high]):
                min_q.pop()
            
            max_q.append(nums[high])
            min_q.append(nums[high])

            if abs(max_q[0] - min_q[0]) > limit:
                while (low < high and abs(max_q[0] - min_q[0]) > limit):
                    if min_q[0] == nums[low]:
                        min_q.popleft()
                    if max_q[0] == nums[low]:
                        max_q.popleft()
                    low += 1

            length = max(length, high - low + 1)   
            
        return length
