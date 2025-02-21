# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque()
        queue.append(root)
        stri = ""

        if not root:
            return stri

        while (queue):
            top = queue.popleft()

            if top != "n":
                stri += str(top.val)
                stri += ","

                if top.left:
                    queue.append(top.left)
                else:
                    queue.append("n")
                
                if top.right:
                    queue.append(top.right)
                else:
                    queue.append("n")
            else:
                stri += "n"
                stri += ","
        
        return stri
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        list = []
        start = 0
        for i in range(len(data)):
            if data[i] == ',':
                if data[start:i] == 'n':
                    list.append((data[start:i]))
                else:
                    list.append(int(data[start:i]))
                start = i + 1
        
        print(list)
        
        root = TreeNode(list[0])
        node = root
        count = 0 
        queue = deque()

        for i in range(1, len(list)):
            if list[i] != "n":
                if count == 0:
                    root.left = TreeNode(list[i])
                    count += 1
                    queue.append(root.left)
                elif count == 1:
                    root.right = TreeNode(list[i])
                    count = 0
                    queue.append(root.right)
                    if queue:
                        root = queue.popleft()
            else:
                if count == 0:
                    root.left = None
                    count += 1
                elif count == 1:
                    root.right = None
                    count = 0
                    if queue:
                        root = queue.popleft()
    
        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
