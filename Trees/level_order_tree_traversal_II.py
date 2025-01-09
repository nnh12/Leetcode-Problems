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
            length = len(queue)
            sublevel = []

            for _ in range(length):
                top = queue.popleft()

                sublevel.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                
            list.append(sublevel)   

        return list[::-1]

    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            return self.bfs(root)
        
