# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node(object):
    def __init__(self, tree_node, val):
        self.tree_node = tree_node
        self.val = val
    
    def get_tree(self):
        return self.tree_node
    
    def get_val(self):
        return self.val

class Solution(object):

    def bfs(self, node):
        list = []
        list.append([])
        queue = deque()
        parent = Node(node, -1)
        queue.append(parent)

        while queue:
            parent = queue.popleft()
            top = parent.get_tree()
            level = parent.get_val() + 1
            
            if level >= len(list):
                list.append([])

            list[level].append(top.val)
            
            if top.left:
                node = Node(top.left, level)
                queue.append(node)
            if top.right:
                node = Node(top.right, level)
                queue.append(node)
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
