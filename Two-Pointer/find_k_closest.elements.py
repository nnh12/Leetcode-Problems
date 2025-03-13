class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = []   
        heapq.heapify(heap)
        gap = abs(x - arr[0])

        for i in arr:
            diff = -1* abs(x - i)
            
            if len(heap) < k:
                heapq.heappush(heap,  (diff, i))
            else:
                top = heap[0]
                largest_diff, index =top
                
                if diff > largest_diff:
                    max = heapq.heappop(heap)
                    val, ic = max
                    heapq.heappush(heap, (diff, i))
                                  
                    
        list = [index for diff, index in heap]
        return sorted(list)
