class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        low = 0
        cur = chars[0]
        k = 0
        index = 0

        for high in range(len(chars)):
            if chars[high] == cur:
                k += 1
            elif chars[high] != cur:
                chars[low] = cur
                index += 1
                low += 1
                if k > 1:
                    for let in str(k):
                        chars[low] = (let)
                        low += 1
                        index += 1

                cur = chars[high]
                k = 1

        if chars[high] == cur:
            chars[low] = cur
            index += 1
            low += 1    

            if k > 1:
                for let in str(k):
                    chars[low] = (let)
                    low += 1
                    index += 1
                    
        return index
        
