class Solution(object):
    def isValid(self, s): 
        make=list()
        pos=-1
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                make.append(ch)
            else:
                if not make:
                    return False
                if ch==')' and make[-1]=='(':
                    make.pop(-1)
                elif ch=='}' and make[-1]=='{':
                    make.pop(-1)
                elif ch==']' and make[-1]=='[':
                    make.pop(-1)
                else:
                    return False
        return not make
           
