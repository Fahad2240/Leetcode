class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat=set(pattern)
        h=[]
        str=''
        pt=0
        for item in s:
            if item==' ':
                h.append(str)
                str=''
                continue
            str=str+item
        for x in range(len(s)):
            if s[x]==' ':
                pt=x
        if pt!=0:
            pt=pt+1
            stt=''
            for x in range(pt,len(s)):
                stt=stt+s[x]
            # print(stt)
            h.append(stt)
        if len(h)==0:
            h.append(s[0])
        # lista=list(set([x for x in h if h.count(x) >= 1]))
        
        self.h=set(h)
        self.pattern=pattern
        dicta={}
        if len(h)!=len(self.pattern) or len(self.h)!=len(pat):
            return False
        else:
            # print(self.h)
            # print(pat)
            key_list=list(h)
            val_list=list(self.pattern)
            
            for x in range(len(key_list)):
                dicta[key_list[x]]=val_list[x]
            # print(dicta)
            for x in range(len(key_list)):
                if dicta[key_list[x]]!=val_list[x]:
                    return False
            return True
