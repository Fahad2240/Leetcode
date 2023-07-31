class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        p=nums[0]
        cnt=0
        for item in nums:
            if item!=p:
                p=item
                cnt+=1
            else:
                cnt+=1
            if cnt>(int)(len(nums)/2):
                return item