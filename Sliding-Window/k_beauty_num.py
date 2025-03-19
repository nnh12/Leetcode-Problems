class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        num_str = str(num)
        cur = num_str[0: k]
        count = 0
        low = 1
        flag = 0

        if num % int(cur) == 0:
            count += 1 

        for i in range(k, len(num_str)):
            while (low < len(cur) - 1 and cur[low] == '0' ):
                flag = 1
                low += 1

            cur = cur[low:len(cur)] + num_str[i]

            if int(cur) != 0 and num % int(cur) == 0:
                count += 1

            if flag:
                low = 0
                flag = 0
            else:
                low = 1
        
        return count
