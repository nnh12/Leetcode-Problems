class Solution(object):
    def __init__(self):
        self.dict = {}
        self.max = 0
        self.char = ""

    
    def add_char(self, char):
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1
        
        if self.dict[char] > self.max:
            self.max = self.dict[char]
            self.char = char

        return True
    
    def remove_char(self,char):
        if char in self.dict:
            self.dict[char] -= 1
            if char == self.char:
                self.max -= 1
            

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = 0 
        left = 0
        
        for right in range(len(s)):
            self.add_char(s[right])

            if (right - left + 1 - self.max > k):
                max_len = max(right - left, max_len)
                self.remove_char(s[left])
                left += 1

        if left == 0:
            max_len = len(s)

        max_len = max(max_len, right - left + 1)
   
        return max_len
