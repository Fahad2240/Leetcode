class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index=-1
        for x in range(len(nums)-1,0,-1):
            if nums[x-1]<nums[x]:
                index=x
                break
        
        if index==-1:
            return nums.sort()
        else:
            # print(index)
            for x in range(len(nums)-1,index-1,-1):
                if nums[x]>nums[index-1]:
                    nums[x],nums[index-1]=nums[index-1],nums[x]
                    # print(index-1)
                    break
            left,right=index,len(nums)-1
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        return nums