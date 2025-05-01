class Solution(object):

    def __init__(self):
        self.matrix = defaultdict(list)

    def build_path(self, times, n, k):
        list = [float('inf')] * (n + 1)
        list[k] = 0
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, [0 , k])
        print(list)

        while heap:
            distance, node = heapq.heappop(heap)
            neighbors = self.matrix[node]

            for n in neighbors:
                distance_n, node_n = n
                cur_distance = distance_n + distance

                if cur_distance < list[node_n]:
                    list[node_n] = cur_distance
                    heapq.heappush(heap, [cur_distance, node_n])
        
        return list


    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        sum = 0 
        for time in times:
            self.matrix[time[0]].append( [time[2], time[1]] )

        print(self.matrix)
        distance = self.build_path(times, n, k)

        for i in range(1, len(distance)):
            if distance[i] == float('inf'):
                return -1

            sum = max(sum, distance[i])
        return sum
