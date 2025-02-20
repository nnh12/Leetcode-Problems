class Node(object):
    def __init__(self, char):
        self.neighbors = {}
        self.char = char
    
    def add_neighbor(self, char, node):
        if char not in self.neighbors:
            self.neighbors[char] = node
    
class WordDictionary(object):

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        char = word[0]
        if char not in self.root:
            node = Node(char)
            self.root[char] = node
            for i in range(1, len(word)):
                curr = Node(word[i])
                node.add_neighbor(word[i], curr)
                node = curr
        else:
            node = self.root[char]

            for i in range(1, len(word)):
                curr_word = word[i]
                if curr_word not in node.neighbors:
                    curr = Node(word[i])
                    node.add_neighbor(curr_word, curr)
                    node = curr
                else:
                    node = node.neighbors[curr_word]

            
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        char = word[0]

        if char in self.root:
            node = self.root[char]
            
            for i in range(1, len(word)):
                curr_word = word[i]
                if curr_word in node.neighbors:
                    node = node.neighbors[curr_word]
                else:
                    return False
                  
        return True
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
