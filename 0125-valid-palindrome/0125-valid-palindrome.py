class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        d=""
        for x in s:
            if  x in alphabet:
                if alphabet.index(x)> 25:
                    d+=alphabet[alphabet.index(x)-26]
                else:
                    d+=alphabet[alphabet.index(x)]
            if x>='0' and x<='9':
                d+=x
        temp=list(reversed(d))
        temp1=''.join(temp)
        print(d)
        
        if temp1==d:
            return True
        return False

//test
