import random
class Codec:

    def __init__(self):
        self.dict= defaultdict(list)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        num = random.randint(1, 10000)
        
        num = str(num)
        while num:
            if num not in self.dict:
                break
            num = random.randint(1, 10000)

        self.dict[num] = longUrl
        return num


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dict[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
