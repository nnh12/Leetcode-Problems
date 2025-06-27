class Solution(object):

    def calc(self, digits, start, mid, end, track):
        if mid >= len(digits):
            return
        
        if mid != start and mid != end:
            num = int(str(digits[start]) + str(digits[mid]) + str(digits[end]) )

            if num not in track:
                track.add(num)
        
        return self.calc(digits, start, mid + 1, end, track)
        

    def compute(self,start, digits, even_set, track):
        if start >= len(digits):
            return
        
        if digits[start] != 0:
            for index, num in even_set:
                if index != start:
                    self.calc(digits, start, 0, index, track)

        return self.compute(start + 1, digits, even_set, track)

    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        track = set()
        even_set = set()
        
        for i in range(len(digits)):
            if digits[i] % 2 == 0:
                even_set.add((i, digits[i]))
        
        self.compute(0, digits, even_set, track)
        
        return len(track)
