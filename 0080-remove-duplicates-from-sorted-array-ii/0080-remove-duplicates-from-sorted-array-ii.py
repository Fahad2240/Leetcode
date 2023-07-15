class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        for x in nums:
            if i==0 or i==1 or nums[i-2]!=x:
                nums[i]=x
                i+=1
        return i
        