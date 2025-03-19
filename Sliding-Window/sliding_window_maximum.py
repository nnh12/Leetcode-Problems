class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        heapq.heapify(heap)
        low = 0
        list = []

        for i in range(k):
            heapq.heappush(heap, -1 * nums[i])

        list.append(-1 * heap[0])
        for i in range(k, len(nums)):
            if (-1 * nums[low]) in heap:
                heap.remove(-1 * nums[low])
            
            heapq.heappush(heap, - 1 * nums[i])
            heapq.heapify(heap)
            list.append(-1 * heap[0])
            low += 1
        
        return list
