class Solution(object):
    def __init__(self):
        self.max_count = 0
        self.char_dict = {}
        self.max_char = ""

    def add_char(self, char):

        if char in self.char_dict:
            self.char_dict[char] += 1
        else:
            self.char_dict[char] = 1

        if self.char_dict[char] > self.max_count:
            self.max_count = self.char_dict[char]
            self.max_char = char
        
        return True

    def remove_char(self, char):
        if char in self.char_dict:
            if self.char_dict[char] > 0:
                self.char_dict[char] -= 1    
        
        if self.max_char == char:
            self.max_count -= 1
        
 
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        max = 0
        right = 0

        for i in range(len(s)):
            left = i
            while (right < len(s) and self.add_char(s[right]) and (right - left + 1 - self.max_count <= k)):
                if (right - left + 1 > max):
                    max = right - left + 1
                print(s[right], right, left, self.char_dict, self.max_count, right - left + 1 - self.max_count)

                right += 1
                                
            right -= 1
            print('here')
            self.remove_char(s[left])
                   
        return max

