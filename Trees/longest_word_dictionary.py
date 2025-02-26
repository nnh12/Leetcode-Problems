class Node(object):
    def __init__(self):
        self.childern = {}
        self.end = False

class Solution(object):

    def __init__(self):
        self.root = Node()
    
    def add_node(self, cur_node, char):
        cur_node.childern[char] = Node()
        cur_node = cur_node.childern[char]
        return cur_node
    
    def comp(self, cur_string, string):
        if len(cur_string) == len(string):
            if cur_string < string:
                string = cur_string
        elif len(cur_string) > len(string):
            string = cur_string
        
        return string

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words)
        print(words)

        count = 0
        string = ""

        for word in words:             
            cur_node = self.root
            cur_string = ""

            if len(word) == 1:
                string = self.comp(word[0], string)
                cur_node = self.add_node(cur_node, word[0])

            if len(word) > 1 and word[0] in cur_node.childern:

                for index in range(len(word)):
                    if index != len(word) - 1 and word[index] in cur_node.childern:
                        cur_string += word[index]
                        cur_node = cur_node.childern[word[index]]
                    
                    elif index == len(word) - 1:
                        cur_node = self.add_node(cur_node, word[index])
                        cur_string += word[index]

                        print(cur_string, string)
                        string = self.comp(cur_string, string)
                    else:
                        break
            
        return string
