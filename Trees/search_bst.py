# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.keep = None

    def search(self, root, val):
        if root == None:
            return

        if root.val == val:
            self.keep = root
        
        self.search(root.right, val)
        self.search(root.left, val)

    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        self.search(root, val)
        return self.keep
