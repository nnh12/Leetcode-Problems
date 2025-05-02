# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        queue = deque()
        queue.append(root)
        count = 0

        while queue:
            sublevel = []
            for _ in range(len(queue)):
                top = queue.popleft()
                sublevel.append(top)

                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
            
            if count % 2 != 0:
                end = len(sublevel) - 1
                for i in range(len(sublevel) / 2):
                    h = sublevel[i]
                    l = sublevel[end]
                    temp = h.val
                    h.val = l.val
                    l.val = temp
                    end -= 1

            count += 1 
        
        return root
                
