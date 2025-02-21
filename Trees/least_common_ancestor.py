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
        print('tree', tree.tree.val, 'tree2', tree2.tree.val)

        while tree or tree2:

            if tree.tree == original2.tree:
                print('1')
                return tree.tree
            elif tree2.tree == original.tree:
                print('2')
                return tree2.tree
            elif tree.tree == tree2.tree:
                print('3')
                return tree.tree

            if tree.parent:
                tree = tree.parent
            if tree2.parent:
                tree2 = tree2.parent
        
        return tree.tree
