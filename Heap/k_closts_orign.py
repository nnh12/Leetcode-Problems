class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        list = []
        heap = []
        heapq.heapify(heap)

        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt( (x)**2 + (y)**2 )
            heapq.heappush(heap, [-1*distance, point] )    

            if len(heap) > k:
                heapq.heappop(heap)

        for h in heap:
            list.append(h[1])

        return list
