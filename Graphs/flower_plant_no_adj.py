class Solution(object):
    
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        matrix = {}
        flowers = {}
        list = []

        for path in paths:
            if path[0] not in matrix:
                matrix[path[0]] = []
                matrix[path[0]].append(path[1])
            else:
                matrix[path[0]].append(path[1])
        
            if path[1] not in matrix:
                matrix[path[1]] = []
                matrix[path[1]].append(path[0])
            else:
                matrix[path[1]].append(path[0])
        
        for i in range(1, n+ 1):
            track = set()
            
            if i in matrix:
                neighbors = matrix[i]
                for n in neighbors:
                    if n in flowers:
                        track.add(flowers[n])
   
            for f in range(1, 5):
                if f not in track:
                    list.append(f)
                    flowers[i] = f
                    break
        
        return list
        
