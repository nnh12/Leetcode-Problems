class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.dict = {}
        self.limit = timeToLive

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId not in self.dict:
            start = currentTime
            end = currentTime + self.limit
            self.dict[tokenId] = [start, end]
        

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.dict:
            start, end = self.dict[tokenId]

            if currentTime < end:
                end = currentTime + self.limit
                self.dict[tokenId] = [start, end]
        
    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        count = 0
        for token in self.dict:
            start, end = self.dict[token]
            
            if currentTime >= start and currentTime < end:
                count += 1

        return count

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
