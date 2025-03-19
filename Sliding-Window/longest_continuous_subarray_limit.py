class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_heap = []
        min = []
        heapq.heapify(max_heap)
        heapq.heapify(min)
        low = 0
        length = 0

        for high in range(len(nums)):
            heapq.heappush(max_heap, -1*nums[high])
            heapq.heappush(min, nums[high])

            if abs((-1 * max_heap[0]) - min[0]) > limit:
                while (low < high and abs((-1 * max_heap[0]) - min[0]) > limit ):
                    max_heap.remove(-1 * nums[low])
                    min.remove(nums[low])
                    heapq.heapify(max_heap)
                    heapq.heapify(min)
                    low += 1
                  
            length = max(length, high - low + 1)
                
        return length
