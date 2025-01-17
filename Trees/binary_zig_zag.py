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
        tree = []

        while queue:
            
            queue_len = len(queue)
            sublevel = []
            
            for _ in range(queue_len):
                top = queue.popleft()
                print("top", top.val)
                sublevel.append(top.val)

                #print(sublevel)

                if top.left:
                    queue.append(top.left)
                    print("left", top.left.val)
                if top.right:
                    queue.append(top.right)
                    print("right", top.right.val)
            
            tree.append(sublevel)
        
        return tree

    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            list = self.bfs(root)
            for i in range(len(list)):
                if i % 2 != 0:
                    sublist = list[i]
                    list[i] = sublist[::-1]
            return list
