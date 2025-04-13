class Solution(object):

    def count_words(self, str):
        count = 0
        for s in str:
            if s == " ":
                count += 1
        
        return count + 1

    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        message = {}
        max_str = ""
        max_sum = 0
        for i in range(len(senders)):
            if senders[i] not in message:
                message[senders[i]] = self.count_words(messages[i])
            else:
                message[senders[i]] += self.count_words(messages[i])
        
        for m in message:
            if max_sum == message[m]:
                max_str = max(max_str, m)
            elif message[m] > max_sum:
                max_sum = message[m]
                max_str = m
        
        return max_str
