class Solution(object):

    def __init__(self):
        self.dict = {}
        self.ref_dict = {}
    
    def add_char(self, char):
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1
    
    def remove_char(self, char):
        if char in self.dict:
            self.dict[char] -= 1
            if self.dict[char] == 0:
                del self.dict[char]
        
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        for i in p:
            if i in self.ref_dict:
                self.ref_dict[i] += 1
            else:
                self.ref_dict[i] = 1

        count = 0
        start = 0
        list = []

        for index in range(len(s)):
            if count < len(p):
                self.add_char(s[index])
                count += 1

                if self.dict == self.ref_dict:
                    list.append(start)
            else:
                self.add_char(s[index])
                self.remove_char(s[start])
                start += 1

                if self.dict == self.ref_dict:
                    list.append(start)

        return list
