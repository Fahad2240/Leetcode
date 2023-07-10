class Codec:
    def __init__(self):
        self.base='http://tinyurl.com'
        self.longtoshort={}
        self.shorttolong={}
    def encode(self, longUrl: str) -> str:
        if longUrl not in self.longtoshort:
            shortUrl=self.base+'/'+str(len(longUrl))
            self.longtoshort[longUrl]=shortUrl
            self.shorttolong[shortUrl]=longUrl
        return self.longtoshort[longUrl]
    def decode(self, shortUrl: str) -> str:
        return self.shorttolong[shortUrl]

