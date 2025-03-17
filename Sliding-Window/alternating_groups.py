class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        count = 0

        for i in range(len(colors)):
            if i == 0 and  (  ([colors[len(colors) - 1 ], colors[i], colors[i + 1]] == [1, 0, 1]) or [colors[len(colors) - 1 ], colors[i], colors[i + 1]] == [0, 1, 0]):
                count += 1
            elif i == len(colors) - 1 and  (([ colors[i - 1], colors[len(colors) - 1], colors[0]] == [1, 0, 1]) or [colors[i - 1], colors[len(colors) - 1], colors[0] ] == [0, 1, 0]):
                count += 1
            elif i > 0 and i < len(colors) - 1 and (([ colors[i - 1], colors[i], colors[i + 1]] == [1, 0, 1]) or [colors[i - 1], colors[i], colors[i + 1] ] == [0, 1, 0]):
                count += 1
         
        
        return count
