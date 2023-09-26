class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store=set()
        l=0
        maxi=0
        for r in range(0,len(s)):
            if s[r] in store:
                while l<r and (s[r] in store):
                    store.remove(s[l])
                    l+=1
            store.add(s[r])
            maxi=max(maxi,r-l+1)
        return maxi