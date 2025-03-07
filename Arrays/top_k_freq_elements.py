class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}

        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        heap = []
        heapq.heapify(heap)
        list = []
        
        for i in dict:
            heapq.heappush(heap, (dict[i], i))

            if len(heap) > k:
                heapq.heappop(heap)

        for i in heap:
            freq, index = i
            list.append(index)

        return list
