class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[]*n
        
        for i in range(n):
            res=[0]*n
            dp.append(res)
            
        for i in range(n-1,-1,-1):
            for j in range(i+1):
                # print(i)
                if i==n-1:
                    dp[i][j]=triangle[i][j]
                else:
                    up=dp[i+1][j]+triangle[i][j]
                    updig=dp[i+1][j+1]+triangle[i][j]
                    dp[i][j]=min(up,updig)
        # print(dp)
        return dp[0][0]
                