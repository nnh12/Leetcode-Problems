class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        index = 0
        list = []

        for i in range(len(code)):
            ret = k
            sum = 0
            index = i
            if k > 0:
                while ret > 0:
                    index += 1
                    if index == len(code):
                        index = 0
                    
                    print(code[index])
                    sum += code[index]
                    ret -= 1
                
                print(' ')
                list.append(sum)

            elif k < 0:
                while ret < 0:
                    index -= 1
                    if index < 0:
                        index = len(code) - 1
                    
                    sum += code[index]
                    ret += 1
                
                list.append(sum)
            
            elif k == 0:
                return [0] * len(code)
        
        return list
