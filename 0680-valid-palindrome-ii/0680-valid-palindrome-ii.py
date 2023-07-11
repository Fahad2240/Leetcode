class Solution(object):
    def validPalindrome(self, s):
        left=0
        right=len(s)-1
        def check(s,left,right):
            while left<right:
                if s[left]==s[right]:
                    left=left+1
                    right=right-1
                else:
                    return False
            return True
        while left<right:
            if s[left]==s[right]:
                left=left+1
                right=right-1
            else:
                x=check(s,left+1,right)
                y=check(s,left,right-1)
                return x or y
        return True
        