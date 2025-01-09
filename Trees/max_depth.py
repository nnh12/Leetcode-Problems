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
        count = 0

        while queue:
            len_q = len(queue)

            for _ in range(len_q):
                top = queue.popleft()

                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
            
            count += 1
        
        return count

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        else:
            return self.bfs(root)
