class Solution(object):

    def bfs(self, node, matrix, n_len):
        queue =  deque()
        queue.append(node)
        all_paths = []

        while queue:
            cur_path = queue.popleft()
            print(cur_path)
            last = cur_path[len(cur_path) - 1]
            neighbors = matrix[last]

            if last == n_len - 1:
                all_paths.append(cur_path)
                continue
            
            for n in neighbors:
                queue.append(cur_path + [n] )

        return all_paths

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        node = 0
        matrix = {}
        graph_matrix = {}
        n_len = len(graph)
        for nodes in graph:
            matrix[node] = nodes
            node += 1
        
        return self.bfs([0], matrix, n_len)
