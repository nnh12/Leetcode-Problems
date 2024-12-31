"""
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        let_list = []
        let = 0
        row = 0
        word = ""
        down = 1

        for _ in range(numRows):
            let_list.append([])
                
        while (let < len(s)):
            for index in range(numRows):
                if let >= len(s):
                    break
                let_list[index].append(s[let])
                let += 1
            
            if numRows >= 2:
                for index in range(numRows -2, 0, -1):
                    if let >= len(s):
                        break
                    let_list[index].append(s[let])
                    let += 1
            elif numRows == 1:
                for index in range(numRows - 1, -1, -1):
                    if let >= len(s):
                        break
                    let_list[index].append(s[let])
                    let += 1
            
        for list in let_list:
            for let in list:
                word += let

        return word   
