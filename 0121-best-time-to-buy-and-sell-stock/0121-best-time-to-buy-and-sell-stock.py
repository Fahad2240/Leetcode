class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini,max_prof,cost=prices[0],0,0
        for x in range(1,len(prices)):
            cost=prices[x]-mini
            max_prof=max(max_prof,cost)
            mini=min(mini,prices[x])
        return max_prof        