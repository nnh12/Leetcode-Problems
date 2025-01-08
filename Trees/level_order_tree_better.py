# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def bfs(self, node):
        if node is None:
            return []

        queue = deque()
        queue.append(node)
        list = []

        while queue:
            sublevel = []
            num_nodes = len(queue)
        
            for _ in range(num_nodes):
                top = queue.popleft()
                sublevel.append(top.val)

                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)

            list.append(sublevel)
            
        return list
        

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            return self.bfs(root)
