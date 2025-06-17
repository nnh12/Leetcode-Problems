class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        queue = deque()

        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = [s[i] , 1, i]
                queue.append(s[i])
            else:
                let, freq, index = dict[s[i]]
                freq += 1
                dict[s[i]] = [let, freq, index]
        
        while queue:
            cur_let = queue.popleft()
            let, freq, index = dict[cur_let]
            if freq == 1:
                return index
        
        return -1
