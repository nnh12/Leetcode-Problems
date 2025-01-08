class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        i=1
        while (i < len(path)):
            if path[i-1] == '/' and path[i] == '/':
                path = path[:i] + path[i+1:]
            else:
                i += 1
        
        i=1
        start = 0
        list = []

        while i < len(path):
            start = i
            while (i < len(path) and path[i] != '/'):
                i += 1
                
            list.append(path[start:i])
            i+=1
        
        stack = []
        index = 0

        #print(list)
        while(index < len(list)):
            if list[index] == ".." and index + 1 < len(list):
                stack.pop()
                stack.append(list[index+1])
                index += 2
            else:
                stack.append(list[index])
                index += 1

        if len(stack) == 1 and stack[0] == "..":
            return "/"
            
        #print(stack)
        path = "/"
        for i in stack:
            if i != '.':
                path += i
                path += "/"

        return path[:len(path) -1]
