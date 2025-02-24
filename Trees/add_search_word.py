class Node(object):
    def __init__(self):
        self.childern = {}
        self.end = False


class WordDictionary(object):

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
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

    
    def dfs(self, index, cur_node, word):
        if index == len(word):
            return cur_node.end
        
        if word[index] == ".":
            for child in cur_node.childern:
                if self.dfs(index + 1, cur_node.childern[child]   , word):
                    return True

        if word[index] in cur_node.childern:
            return self.dfs(index + 1, cur_node.childern[word[index]], word  )
        else:
            return False


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur_node = self.root
        return self.dfs(0, cur_node, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
