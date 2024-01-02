class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for x in range(0,len(nums)):
            for y in range(x,len(nums)):
                if nums[x]>nums[y]:
                    temp=nums[x]
                    nums[x]=nums[y]
                    nums[y]=temp
    
        