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
            return 0

        if root.val == val:
            return root
        
        left = self.search(root.left, val)
        if left:
            return left
        right = self.search(root.right, val)
        
        if right:
            return right
        

    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        return self.search(root, val)
        
