class Solution(object):
    def __init__(self):
        self.list = list()

    def process(self, node):
        if node is None:
            return
        
        self.process(node.left)
        self.list.append(node.val)
        self.process(node.right)
    
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.process(root)
        return self.list
