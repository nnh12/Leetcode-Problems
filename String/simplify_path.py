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
        for file in list:
            if file != ".." and file != ".":
                stack.append(file)
            elif file== ".." and stack:
                stack.pop()
            print(stack)
        
        str = "/"

        for file in stack:
            str += file
            str += "/"
        
        if str == "/":
            return str

        return str[:len(str) -1]
