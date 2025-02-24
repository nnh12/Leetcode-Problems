class Node(object):
    def __init__(self):
        self.childern = {}
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur_node = self.root
        for c in word:
            if c not in cur_node.childern:
                cur_node.childern[c] = Node()
                cur_node = cur_node.childern[c]
            else:
                cur_node = cur_node.childern[c]
        
        cur_node.end = True
    
    def dfs(self, i, cur_node, word, prefix):
        if i == len(word):
            if prefix:
                return True
            else:
                return cur_node.end
        
        if word[i] in cur_node.childern:
            return self.dfs(i + 1,  cur_node.childern[word[i]], word, prefix)
        else:
            return False

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur_node = self.root
        return self.dfs(0, cur_node, word, False )

        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur_node = self.root
        return self.dfs(0, cur_node, prefix, True)
        
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
