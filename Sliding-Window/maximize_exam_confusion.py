class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """

        T = 0
        F = 0
        k_num = 0
        low = 0
        length = 0

        for high in range(len(answerKey)):
            if answerKey[high] == 'T':
                T += 1
            else:
                F += 1
            
            k_num = min(T, F)

            while (low <= high and k_num > k):
                if answerKey[low] == 'T':
                    T -= 1
                else:
                    F -= 1

                k_num = min(T, F)
                low += 1
            
            length = max(length, T + F)

        return length
