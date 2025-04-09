class Solution(object):

    def __init__(self):
        self.matrix = {}
        self.visit = set()
        self.bomb = []

    def check_node(self, node1, node2):
        x1, y1, r1 = node1[:3]
        x2, y2, r2 = node2[:3]
        distance = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

        if distance <= r1:
            return True
        else:
            return False

    def dfs(self, node):
        queue = deque()
        queue.append(node)
        self.visit = set()
        self.visit.add(node)
        count = 0

        while queue:
            top = queue.popleft()
            print(top, self.bomb[top], self.matrix[top])
            neighbors = self.matrix[top]
            count += 1
            for n in neighbors:
                if n not in self.visit:
                    self.visit.add(n)
                    queue.append(n)
    
        return count

    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        node = 0
        check_node = 1
        max_sum = 0
        self.bomb = bombs

        for node in range(len(bombs)):
            for check_node in range(len(bombs)):
                if self.check_node(bombs[node], bombs[check_node]):
                    if node not in self.matrix:
                        self.matrix[node] = set()
                    self.matrix[node].add(check_node)
                if self.check_node(bombs[check_node], bombs[node]):
                    if check_node not in self.matrix:
                        self.matrix[check_node] = set()
                    self.matrix[check_node].add(node)

            check_node += 1                 
        
        for key in self.matrix:
            if key not in self.visit:
                max_sum = max(max_sum, self.dfs(key))
        
        return max_sum
