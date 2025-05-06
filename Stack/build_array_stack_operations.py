    """
    Python3 solution to
    Build an Array With Stack Operations
    https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=problem-list-v2&envId=stack
    """

class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = []
        list = []
        index = 1
        count = 0

        while stack != target:
            if index <= n:
                stack.append(index)
                list.append('Push')

                if index != target[count]:
                    stack.pop()
                    list.append('Pop')
                else:
                    count += 1
                index += 1
            else:
                return list
              
        return list
            
