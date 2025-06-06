class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        list = []
        stack = []
        for i in prices:
            list.append(i)
        
        for i in range(len(prices)):
            cur_element = prices[i]

            while stack and prices[stack[-1]] >= cur_element:
                ele = stack.pop()
                list[ele] = prices[ele] - cur_element 
            
            stack.append(i)
        
        return list
