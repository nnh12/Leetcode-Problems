"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):

    def bfs(self, root):
        queue = deque()
        queue.append(root)
        new_node = Node(root.val)
        new_tree = deque()
        new_tree.append(new_node)
        prev = None

        while queue:
            len_queue = len(queue)

            for i in range(len_queue):
                top = queue.popleft()
                new_top = new_tree.popleft()

                if i == 0:
                    prev = new_top
                elif i == (len_queue - 1):
                    prev.next = new_top
                    new_top.next = None
                else:
                    prev.next = new_top
                    prev = new_top

                if top.left:
                    queue.append(top.left)
                    new_top.left = top.left
                    new_tree.append(new_top.left)
                if top.right:
                    queue.append(top.right)
                    new_top.right = top.right
                    new_tree.append(new_top.right)
        
        return new_node

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        return self.bfs(root)
