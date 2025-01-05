class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        i = 1
        list = []
        stack = []
        string = ""

        while (i < len(path)):
            if (path[i] == '/' and path[i-1] == '/'):
                path = path[:i] + path[i+1:]
            else:
                i += 1
        
        print(path)
        i = 0
        while (i < len(path)):
            if path[i] == '/':
                list.append(path[i])
                i += 1
            else:
                for index in range(i, len(path)):
                    if path[index] == '/':
                        break
                list.append(path[i:index])
                i = index + 1

        print(list)
        index = 0
        while (index < len(list)):
            if list[index] == ".." and index != 1:
                stack.pop()
                stack.append(list[index + 1])
                index += 2
            else:
                stack.append(list[index])
                index += 1
        
        print(stack)

        for index in range(len(stack)):
            string += stack[index]
            if index >= 1:
                string += '/'
            
        return string[:len(string)-1]
        
