class Node(object):
    def __init__(self, char):
        self.char = ""
        self.neighbors = {}
        self.end = False
    
    def add_neighbor(self, char, node):
        if char not in self.neighbors:
            self.neighbors[char] = node

    def get_neighbors(self):
        return self.neighbors

class Trie(object):

    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        first_char = word[0]
        if first_char not in self.root:
            node = Node(first_char)
            temp = node
            for i in range(1, len(word)):
                curr_node = Node(word[i])
                node.add_neighbor(word[i], curr_node)
                node = curr_node
            
            node.end = True
            self.root[first_char] = temp
        
        else:
            node = self.root[first_char]
            for index in range(1, len(word)):
                neighbor = node.get_neighbors()
                if (neighbor.get(word[index])):
                    node = neighbor[word[index]]
                else:
                    curr_node = Node(word[index])
                    node.add_neighbor(word[index], curr_node )
                    node = curr_node

            node.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        first_char = word[0]
        if first_char in self.root:

            node = self.root[first_char]
            for index in range(1, len(word)):
                curr_word = word[index]
                if curr_word not in node.neighbors:
                    return False
                node = node.neighbors[curr_word]

            return node.end
        
        return False

        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        first_char = prefix[0]
        if first_char in self.root:
            node = self.root[first_char]

            for index in range(1, len(prefix)):
                curr_word = prefix[index]
                if curr_word not in node.neighbors: 
                    return False
                
                node = node.neighbors[curr_word]
            
            return True
        else:
            return False
        



'''
apple
apn 
appe

a -> p -> p -> l -> e
     |    |
     n    e
'''

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
