class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[]*m
        for x in range(m):
            res=[0]*n
            dp.append(res)
            
        
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0 and obstacleGrid[i][j]!=1:
                    dp[i][j]=1
                elif obstacleGrid[i][j]==0:
                    up=0
                    left=0
                    if i-1>=0 and obstacleGrid[i-1][j]!=1:
                        up=dp[i-1][j]
                    if j-1>=0 and obstacleGrid[i][j-1]!=1:
                        left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[m-1][n-1]
                    