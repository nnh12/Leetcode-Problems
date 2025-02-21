# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node(object):
    def __init__(self, tree, parent):
        self.tree = tree
        self.parent = parent


class Solution(object):

    def bfs(self, root, key):
        new = Node(root, None)
        queue = deque()
        queue.append([root, new])

        while queue:
            top, new = queue.popleft()

            if top == key:
                return new

            if top.left:
                left = Node(top.left, new)
                if top.left == key:
                    return left
                queue.append([top.left, left])
            if top.right:
                right = Node(top.right, new)
                if top.right == key:
                    return right
                queue.append([top.right, right])
        
        return new

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        original = self.bfs(root, p)
        original2 = self.bfs(root, q)

        tree = original
        tree2 = original2
        set1 = set()

        while tree or tree2:
            if tree.tree in set1:
                return tree.tree
            elif tree2.tree in set1:
                return tree2.tree
            elif tree.tree == tree2.tree:
                return tree.tree

            if tree.parent:
                set1.add(tree.tree)
                tree = tree.parent
            if tree2.parent:
                set1.add(tree2.tree)
                tree2 = tree2.parent

        return tree.tree
