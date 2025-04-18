class NumberContainers(object):

    def __init__(self):
        self.num = {}
        self.indices = {}

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if number not in self.num:
            heap = []
            heapq.heapify(heap)
            self.num[number] = heap
        
        heapq.heappush(self.num[number], (index, number))
        self.indices[index] = number
        

    def find(self, number):
        """
        :type number: int
        """
        if number not in self.num:
            return -1
        
        heap = self.num[number]

        while heap:
            heap_index, heap_num = heap[0]
            if heap_num == self.indices[heap_index] :
                return heap_index
            heapq.heappop(heap)

        return -1
