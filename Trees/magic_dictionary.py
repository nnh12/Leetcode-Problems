class Node(object):
    def __init__(self):
        self.childern = {}
        self.end = False

class MagicDictionary(object):
    def __init__(self):
        self.root = Node()
        
    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        root = self.root
        for word in dictionary:
            cur_node = self.root

            for c in word:
                if c not in cur_node.childern:
                    cur_node.childern[c] = Node()
                    cur_node = cur_node.childern[c]
                else:
                    cur_node = cur_node.childern[c]
            
            cur_node.end = True

    def dfs(self, i, word, cur_node, flag):
        if i == len(word):
            if flag == 0:
                return cur_node.end
            else:
                return False
        
        if word[i] not in cur_node.childern and flag > 0:
            flag -= 1
            for child in cur_node.childern:
                if self.dfs(i + 1, word, cur_node.childern[child], flag):
                    return True

        if word[i] in cur_node.childern:
            return self.dfs(i + 1, word, cur_node.childern[word[i]], flag)
        else:
            return False
            

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        node = self.root
        return self.dfs(0 , searchWord, node, 1)
        
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
