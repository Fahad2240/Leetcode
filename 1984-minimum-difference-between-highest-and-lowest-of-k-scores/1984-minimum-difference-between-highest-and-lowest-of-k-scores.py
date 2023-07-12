class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        mina=float('inf')
        for x in range(0,len(nums)):
            if x+k-1<len(nums):
                mina=min(mina,(nums[x+k-1]-nums[x]))
            else:
                break
        return mina
            
                
        