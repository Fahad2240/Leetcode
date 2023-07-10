class Solution:
    def romanToInt(self, s: str) -> int:
        self.map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        sum=0
        rs = s[::-1]
        i=0
        while i<len(rs):
            d=self.map[rs[i]]
            # print(i)
            # print(rs[i], d)
            if i+1<len(rs):
                if rs[i]=='V' and rs[i+1]=='I':
                    d=4
                    i=i+1
                elif rs[i]=='X' and rs[i+1]=='I':
                    d=9
                    i=i+1
                elif rs[i]=='L' and rs[i+1]=='X':
                    d=40
                    i=i+1
                elif rs[i]=='C' and rs[i+1]=='X':
                    d=90
                    i=i+1
                elif rs[i]=='D' and rs[i+1]=='C':
                    d=400
                    i=i+1
                elif rs[i]=='M' and rs[i+1]=='C':
                    d=900
                    i=i+1
            
            i=i+1
            sum=sum+d
            # print(sum)
        return sum
