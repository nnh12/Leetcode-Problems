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
            self.max -= 1
            max = self.max

            for key in self.dict:
                if self.dict[key] > max:
                    self.char = key
                    self.max = self.dict[key]
    
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max = 0 
        right = 0
        
        for left in range(len(s)):

            while (right < len(s) and self.add_char(s[right]) and (right - left + 1 - self.max <= k )  ):
                print(right, left, self.dict, self.max, self.char)
                right += 1
            
            print(right, left, self.dict, self.max, right - left + 1 - self.max, 'end')
            self.remove_char(s[left])
               
        return max

