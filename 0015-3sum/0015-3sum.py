class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        y=len(nums)-1
        new=[]
        dicta={}
        for pos in range(0,len(nums)):
            items=nums[pos]
            # seta=[]
            left=pos+1
            right=y
            rqr=0
            if items<0:
                rqr=abs(items)
            elif items>0:
                rqr=0-items
            else:
                rqr=0
            while left<right:
                if nums[left]+nums[right]>rqr:
                    right-=1
                elif nums[left]+nums[right]<rqr:
                    left+=1
                else:
                    seta=[]
                    seta.append(nums[pos])
                    seta.append(nums[left])
                    seta.append(nums[right])
                    if (nums[pos],nums[left],nums[right]) not in dicta:
                        dicta[(nums[pos],nums[left],nums[right])]=True
                        new.append(seta)
                    # break
                    left+=1
                

        return new