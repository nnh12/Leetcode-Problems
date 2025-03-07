class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        heapq.heapify(heap)

        for i in nums:
            heapq.heappush(heap, i)

            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in heap:
            return i
