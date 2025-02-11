class Trie(object):

    def __init__(self):
        self.dict = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word not in self.dict:
            self.dict[word] = 1

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for key in self.dict:
            if key == word:
                return True
        
        return False
        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        for word in self.dict:
            print(word, prefix)
            if word[0] == prefix[0]:
                right = 0
                while (right < len(prefix) and right > len(word) and prefix[right] == first_word[right]):
                    right += 1
                
                print(word, prefix, right)
                if (right == len(prefix) - 1):
                    return True
        

        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
