
class Solution(object):

    def __init__(self):
        self.queue = deque()
        self.visit = {}
        self.matrix = []
    
    def bfs(self, node):
        if node is None:
            return None

        self.visit[node] = Node(node.val)
        self.queue.append(node)

        while self.queue:
            front = self.queue.popleft()

            for neighbor in front.neighbors:
                if neighbor not in self.visit:
                    self.visit[neighbor] = Node(neighbor.val)
                    self.queue.append(neighbor)          
                self.visit[front].neighbors.append(self.visit[neighbor])

        return self.visit[node]

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        return self.bfs(node)
