# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def dfs(self, root, node):
        stack = []
        stack.append([root, node])

        while stack:
            full, sub = stack.pop()

            if full.left and sub.left:
                if full.left.val != sub.left.val:
                    return False
                stack.append([full.left, sub.left])

            if full.right and sub.right:
                if full.right.val != sub.right.val:
                    return False
                stack.append([full.right, sub.right])

            if (not full.right and sub.right) or (not full.left and sub.left) or (not sub.right and full.right) or (full.left and not sub.left):
                return False
        return True


    def isSubtree(self, root, subroot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque()
        queue.append(root)

        while queue:
            top = queue.popleft()

            if top == subroot or top.val == subroot.val:
                if self.dfs(top, subroot):
                    return True
            
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)

        return False
        
