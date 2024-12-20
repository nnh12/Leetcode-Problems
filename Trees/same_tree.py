
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Input: p = [1,2,3], q = [1,2,3]
# Output: true

class Solution(object):

    def process(self, node):
        queue = deque()
        queue.append(node)
        list = []

        while queue:
            front = queue.popleft()

            if front:
                list.append(front.val)
                if front.left:
                    queue.append(front.left)
                else:
                    queue.append(None)
                if front.right:
                    queue.append(front.right)
                else:
                    queue.append(None)
            else:
                list.append(None)

        return list

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        list1 = self.process(p)
        list2 = self.process(q)
        print(list1)
        print(list2)

        if list1 == list2:
            return True
        else:
            return False
