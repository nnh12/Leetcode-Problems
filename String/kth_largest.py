class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        heap = []
        heapq.heapify(heap)

        for n in nums:
            n = int(n)
            heapq.heappush(heap, -1*n)
        
        while (k > 1 and len(heap) > 0 ):
            heapq.heappop(heap)
            k -= 1
        
        return str(-1*heap[0])
