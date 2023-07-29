class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(0,len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        n=len(matrix)-1
        x=(int)(n/2)+1
        print(x)
        for i in range(0,n+1):
            for j in range(0,x):
                matrix[i][j],matrix[i][n-j]=matrix[i][n-j],matrix[i][j]
            
        