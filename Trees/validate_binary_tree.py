# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class ParentNode(object):
    def __init__(self, val=0, right_dir=False):
        self.val = val
        self.left = None
        self.right = None
        self.parent = []
        self.right_dir = None
        self.dir = []

    def add_parent(self, val):
        self.parent.append(val)
    
    def add_dir(self, val):
        self.dir.append(val)

    def get_parent(self):
        return self.parent
    
    def get_dir(self):
        return self.dir
    
    def add_list(self, node, dor):
        self.parent.extend(node)
        self.dir.extend(dor)
    
    def print_1(self, n):
        print(n, [node for node in self.parent], [node for node in self.dir])
    

class Solution(object):

    def bfs(self, node):
        queue = deque()
        tree = ParentNode(node.val)
        queue.append([node, tree])

        while queue:
            top, tree = queue.popleft()
            
            if top.right:
                tree.right = ParentNode(top.right.val)
                tree.right.add_parent(tree.val)
                tree.right.add_dir(True)

                if tree.get_parent():
                    tree.right.add_list(tree.get_parent(), tree.get_dir())
            
                cur_val = top.right.val
                dir_list = tree.right.get_dir()
                parent_val = tree.right.get_parent()
    
                for index in range(len(parent_val)):
                    if (dir_list[index] and cur_val <= parent_val[index]) or (not dir_list[index] and cur_val >= parent_val[index]):
                        return False
                
                queue.append([top.right, tree.right])
            
            if top.left:
                tree.left = ParentNode(top.left.val, False)
                tree.left.add_parent(tree.val)
                tree.left.add_dir(False)

                if tree.get_parent():
                    tree.left.add_list(tree.get_parent(), tree.get_dir())
                
                cur_val = top.left.val
                dir_list = tree.left.get_dir()
                parent_val = tree.left.get_parent()

                for index in range(len(parent_val)):
                    if (dir_list[index] and cur_val <= parent_val[index]) or (not dir_list[index] and cur_val >= parent_val[index]):
                        return False

                queue.append([top.left, tree.left])

        return True

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.bfs(root)
        
        
