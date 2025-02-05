class Solution(object):

    def __init__(self):
        self.dict = {}
        self.ref_dict = {}
    
    def add_char(self, char):
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1
    
    def add_char_ref(self, char):
        if char in self.ref_dict:
            self.ref_dict[char] += 1
        else:
            self.ref_dict[char] = 1

    def remove_char(self,char):
        if char in self.dict:
            self.dict[char] -= 1
            if self.dict[char] == 0:
                del self.dict[char]

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        start = 0
        count = 0
        list = []

        for str in s1:
            self.add_char_ref(str)
            
        for index in range(len(s2)):
            if count < len(s1):
                self.add_char(s2[index])
                count += 1

                if self.dict == self.ref_dict:
                    return True
            else:
                self.add_char(s2[index])
                self.remove_char(s2[start])
                start += 1

                if self.dict == self.ref_dict:
                    return True
        
        return False
