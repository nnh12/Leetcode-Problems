"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):

    def __init__(self):
        self.queue = deque()
        self.visit = list()
        self.matrix = []
    
    def bfs(self, node):
        if node is None:
            return None

        self.visit.append(node)
        self.queue.append(node)

        while self.queue:
            front = self.queue.popleft()
            neighbors = front.neighbors
            neighbors = sorted(neighbors, key=lambda node: node.val)
            list = []
            
            for node in neighbors:
                list.append(node)
                if node not in self.visit:
                    self.visit.append(node)
                    self.queue.append(node)

            new_node = Node(front.val, list)
            self.matrix.append(new_node)

        self.matrix = sorted(self.matrix, key=lambda node:node.val)
        
        return self.matrix[0]
        
