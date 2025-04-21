class Solution(object):

    def bfs(self, node, rooms):
        queue = deque()
        queue.append(node)
        count = 0
        visit = set()
        visit.add(node)

        while queue:
            top = queue.popleft()
            neighbors = rooms[top]
            print(top, neighbors)
            count += 1

            for n in neighbors:
                if n not in visit:
                    visit.add(n)
                    queue.append(n)

        return count

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        num = self.bfs(0, rooms)
        print(num, len(rooms))
        if num != len(rooms):
            return False
        return True
        
