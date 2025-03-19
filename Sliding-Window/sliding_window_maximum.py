class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = deque()
        list = []
        end = 1
        front = k - 1

        for i in range(k):
            while (queue and nums[queue[-1]] < nums[i]):
                queue.pop()
            queue.append(i)

        for i in range(k, len(nums)):
            list.append(nums[queue[0]])
            if queue[0] < end:
                queue.popleft()

            while (queue and nums[queue[-1]] < nums[i]):
                queue.pop()

            queue.append(i)
            end += 1

        list.append(nums[queue[0]])
        return list
