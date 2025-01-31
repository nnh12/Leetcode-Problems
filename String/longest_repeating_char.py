class Solution(object):
    def __init__(self):
        self.dict = {}
        self.max = 0
    
    def add_char(self, char):
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1
        
        self.max = max(self.max, self.dict[char])
    
    def remove_char(self, char):
        if char in self.dict:
            self.dict[char] -= 1
        
        max = 0
        for keys in self.dict:
            if self.dict[keys] > max:
                max = self.dict[keys]
        
        self.max = max


    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        win_size = 0
        right, left = 0, 0
        
        while (right < len(s)):

            num_changes = (right - left + 1) - self.max

            if (right- left + 1 > win_size):
                print(self.max)
                print(right, left)
                print(" ")
                win_size = right-left + 1

            if (num_changes > k):
                self.remove_char(s[left])
                left += 1
            else:
                self.add_char(s[right])
                right += 1

        print(self.max)
        return win_size
