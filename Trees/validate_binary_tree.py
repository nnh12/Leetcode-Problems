# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class ParentNode(object):
    def __init__(self, val=0, parent=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = []
    
    def add_node_left(self, node):
        self.left = node
    
    def add_node_right(self, node):
        self.right = node

    def add_parent(self, val):
        self.parent.append(val)
    
    def get_parent(self):
        return self.parent
    

class Solution(object):

    def bfs(self, node):
        queue = deque()
        parent_tree = ParentNode(node.val)
        queue.append([node, parent_tree])

        while queue:
            top, parent = queue.popleft()
            
            if top.left:
                parent.left = ParentNode(top.left.val)
                parent.left.add_parent(top.val)
                if parent.get_parent():
                    parent.left.add_parent(parent.get_parent())

                print(top.left.val, parent.left.get_parent())                
                
                queue.append([top.left, parent.left])
                
            if top.right:
                parent.right = ParentNode(top.right.val)
                parent.right.add_parent(top.val)
                if parent.get_parent():
                    parent.right.add_parent(parent.get_parent())

                print(top.right.val, parent.right.get_parent())

                queue.append([top.right, parent.right])
        
        return parent_tree

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        tree = self.bfs(root)
        print(' ')
        self.bfs(tree)
        
        
