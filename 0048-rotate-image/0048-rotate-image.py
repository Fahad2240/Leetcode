class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # new=[[None for i in range(len(matrix))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(0,i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j],matrix[i][len(matrix)-j-1]=matrix[i][len(matrix)-j-1],matrix[i][j]
        print(matrix)
                # print(matrix[i][len(matrix)-1-j])
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        