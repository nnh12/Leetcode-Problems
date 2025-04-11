class Solution(object):
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        # time O(v.k+e.log(k)), space O(v+e+k)
        graph = {}
        for u, v in edges:  # O(e)
            if vals[v] > 0:
                graph[u] = graph.get(u, []) + [vals[v]]
            if vals[u] > 0:
                graph[v] = graph.get(v, []) + [vals[u]]
        ans = -float('inf')
        for v in range(len(vals)):  # O(v)
            cur_max = vals[v]
            if k > 0 and v in graph:
                min_heap = []
                for val in graph[v]:  # O(e)
                    if len(min_heap) < k:
                        heapq.heappush(min_heap, val)  # O(log(k))
                    elif val > min_heap[0]:
                        heapq.heapreplace(min_heap, val)  # O(log(k))
                for val in min_heap:  # O(k)
                    cur_max += val
            ans = max(ans, cur_max)
        return ans
