class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=0
        for x in nums:
            sum+=x
            if sum<0:
                sum=0
            maxi=max(maxi,sum)
        if maxi==0:
            maxi=max(nums)
        return maxi
        # return 0