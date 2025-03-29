class Solution(object):

    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        matrix = {}

        for edge in edges:
            if edge[0] not in matrix:
                matrix[edge[0]] = []
            
            if edge[1] not in matrix:
                matrix[edge[1]] = []

            matrix[edge[0]].append(edge[1])
            matrix[edge[1]].append(edge[0])

        queue = deque()
        queue.append(source)
        visit = set()
        visit.add(source)

        while (queue):
            top = queue.popleft()

            if top == destination:
                return True

            neighbors = matrix[top]
            for n in neighbors:
                if n not in visit:
                    queue.append(n)  
                    visit.add(n)  

        return False
