class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        list = []
        answer = [0] * len(boxes)

        for i in range(len(boxes)):
            if boxes[i] == '1':
                list.append(i)
        
        for i in range(len(boxes)):
            count = 0
            for ones in list:
                if ones != i:
                    count += abs(i - ones)
            answer[i] = count
        
        return answer
