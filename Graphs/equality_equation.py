class Solution(object):
    def __init__(self):
        self.matrix = {}

    def dfs(self, node, node2):
        queue = deque()
        queue.append(node)
        visit = set()
        visit.add(node)

        while queue:
            top = queue.popleft()
            if top == node2:
                return False

            neighbors = self.matrix[top]

            for n in neighbors:
                if n not in visit:
                    visit.add(n)
                    queue.append(n)

        return True

    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        for equation in equations:
            fir_char = equation[0]
            equal = equation[1]
            sec_char = equation[3]

            if fir_char not in self.matrix:
                self.matrix[fir_char] = set()
            if sec_char not in self.matrix:
                self.matrix[sec_char] = set()
            if equal == '=':    
                self.matrix[fir_char].add(sec_char)
                self.matrix[sec_char].add(fir_char)

        for equation in equations:
            fir_char = equation[0]
            equal = equation[1]
            sec_char = equation[3]

            if equal == '!' and not self.dfs(fir_char, sec_char):
                return False
        
        return True
