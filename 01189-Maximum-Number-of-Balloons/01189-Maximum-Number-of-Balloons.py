class Solution(object):
    def maxNumberOfBalloons(self, text):
        take={'b','a','l','o','n'}
        dicta={}
        for item in take:
            c=0
            for x in text:
                if x==item:
                    c=c+1
            dicta[item]=c
        if dicta['b']==0 or dicta['a']==0 or dicta['l']==0 or dicta['o']==0 or dicta['n']==0:
            return 0
        hisab=[]
        hisab.append(dicta['b'])
        hisab.append(dicta['a'])
        hisab.append(dicta['l'])
        hisab.append(dicta['o'])
        hisab.append(dicta['n'])
        x=(min(dicta, key=dicta.get))
        if x=='l' or x=='o':
            m=dicta[x]/2
        else:
            m=dicta[x]
        d=min(dicta['l']/2,dicta['o']/2)
        if m>d:
            return d
        else:
            if dicta['l']<2 or dicta['o']<2:
                return 0
            else:
                return m
        
        """
        :type text: str
        :rtype: int
        """
