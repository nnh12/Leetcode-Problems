class Node(object):
    def __init__(self, char):
        self.char = ""
        self.neighbors = {}
    
    def add_neighbor(self, char, node):
        if char not in self.neighbors:
            self.neighbors[char] = node

    def get_neighbors(self):
        return self.neighbors
    
    def get_char(self):
        return self.char


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
            copy = node
            for i in range(1, len(word)):
                curr_node = Node(word[i])
                node.add_neighbor(word[i], curr_node)
                node = curr_node
            
            self.root[first_char] = copy
        
        else:
            node = self.root[first_char]
            for index in range(1, len(word)):
                

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        first_char = word[0]
        if first_char in self.root:
            print(first_char)
            node = self.root[first_char]
            for index in range(1, len(word)):
                neighbor = node.get_neighbors()
                print(neighbor)
                if (neighbor.get(word[index])):
                    print(word[index])
                else:
                    return False
                
                node = neighbor[word[index]]

        return True

        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
