class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        large=float(inf)
        def markrow(x):
            for col in range(len(matrix[x])):
                if matrix[x][col]!=0:
                    matrix[x][col]=large
        def markcol(y):
            for row in range(len(matrix)):
                if matrix[row][y]!=0:
                    matrix[row][y]=large
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y]==0:
                    markrow(x)
                    markcol(y)
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y]==large:
                    matrix[x][y]=0
        