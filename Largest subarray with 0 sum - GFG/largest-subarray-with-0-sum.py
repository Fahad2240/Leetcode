#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        maxi=0
        hash={}
        p_sum=0
        for x in range(0,len(arr)):
            p_sum+=arr[x]
            if p_sum==0:
                maxi=x+1
            elif p_sum not in hash:
                hash[p_sum]=x
            else:
                maxi=max(maxi,x-hash[p_sum])
        return maxi
                

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends