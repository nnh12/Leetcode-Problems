class Node(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Solution(object):

    def __init__(self):
        self.root = Node()


    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words)
        print(words)

        if len(words[0]) != 1:
            return ""

        count = 0
        cur_node = self.root
        str = ""
        for word in words:
            for c in range(count + 1, len(word) -   ):
                if word[c] not in cur_node.children:
                    cur_node.children[c] = Node()
                    cur_node = cur_node.children[c]
                    str += word[c]
            
            count += 1
        
        return str
