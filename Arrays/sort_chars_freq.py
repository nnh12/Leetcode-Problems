class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}

        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        heap = []
        for i in dict:
            heapq.heappush(heap, (dict[i], i))
        
        maximum = heapq.nlargest(len(heap), heap)
        string = ""

        for i in maximum:
            freq, letter = i
            for __ in range(freq):
                string += letter
        
        return string
