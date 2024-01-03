class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,left=0,0
        bottom,right=len(matrix)-1,len(matrix[0])-1
        new=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                new.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                new.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    new.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in range(bottom,top-1,-1):
                    new.append(matrix[l][left])
                left+=1
        return new
            