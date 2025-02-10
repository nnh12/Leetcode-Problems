# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):


    def bfs(self, node):
        queue = deque()
        queue.append(node)

        while queue:
            top = queue.popleft()
            
            if top:
                temp = top.right
                top.right = top.left
                top.left = temp
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                

    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        self.bfs(root)
        return root        
