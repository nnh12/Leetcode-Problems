# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def bfs(self, root):
        queue = deque()
        queue.append(root)
        list = []

        while queue:
            top = queue.popleft()
            list.append(top.val)

            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        
        return list

    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        if not root:
            return []
        else:
            list = sorted(self.bfs(root))
            return list[k-1]
