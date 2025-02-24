# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.list = []

    def preorder(self, node):
        if node is None:
            return
        self.list.append(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        node = root
        self.preorder(root)

        for i in range (1, len(self.list)):
            root.right = TreeNode(self.list[i])
            root = root.right
        
        if node and node.left:
            node.left = None
