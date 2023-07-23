class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        big=[]
        for x in range(0,numRows+1):
            sub=[]
            for i in range(0,x):
                if i==0 or i==x-1:
                    sub.append(1)
                else:
                    sub.append(big[x-1][i-1]+big[x-1][i])
            big.append(sub)
        big.pop(0)
        return big
                    
        