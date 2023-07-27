class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # c_0,c_1,c_2=0,0,0
        # for color in nums:
        #     if color==0:
        #         c_0+=1
        #     elif color==1:
        #         c_1+=1
        #     else:
        #         c_2+=1
        # # print(c_0," ",c_1," ",c_2)
        # for x in range(0,c_0):
        #     nums[x]=0
        # for y in range(c_0,c_0+c_1):
        #     nums[y]=1
        # for z in range(c_1,c_1+c_2):
        #     nums[z]=2
        low,mid,high=0,0,len(nums)-1
        for x in range(0,len(nums)):
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
                