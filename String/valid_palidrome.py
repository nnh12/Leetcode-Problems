class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # isalnum() for alpha numeric
        # lower() for lower case
        # upper() for upper case
        # isdigit() for number
        # isalpha for if it is letter
        left = 0
        right = len(s) - 1

        while ( left < right):

            while ( left < right and (s[left] == ' ' or not s[left].isalnum() )  ):
                left += 1

            while (left < right  and (s[right] == ' ' or not s[right].isalnum()  )  ):
                right -= 1
            
            if (lower(s[left]) != lower(s[right])):
                return False
            else:
                left += 1
                right -= 1

        return True
