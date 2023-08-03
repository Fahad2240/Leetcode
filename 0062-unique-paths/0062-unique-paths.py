class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fact=1
        value=m+n-2
        choose=m-1 
        for i in range(1,choose+1):
            fact*=(value-choose+i)/i
        return round(fact)
        