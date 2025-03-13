class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        index = 0
        sum = 0
        ret = k
        
        if ret > 0:
            while (ret > 0):
                index += 1
                if index == len(code):
                    index = 0

                sum += code[index]
                ret -= 1
        elif ret < 0:
            while (ret < 0):
                index -= 1
                if index < 0:
                    index = len(code) - 1

                sum += code[index]
                ret += 1
        elif ret == 0:
            return [0] * len(code) 

        list = []
        list.append(sum)
        
        for i in range(1, len(code)):
            if k > 0:
                index += 1
                if index == len(code):
                    index = 0
                
                sum += (code[index] - code[i])
                list.append(sum)
            else:
                index -= 1
                if index < 0:
                    index = len(code) - 1
                
                print(index)
                sum += (code[index] - code[i])
                list.append(sum)
            
        return list
