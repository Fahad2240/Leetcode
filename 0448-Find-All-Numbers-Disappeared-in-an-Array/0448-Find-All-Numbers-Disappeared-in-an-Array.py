class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index=abs(nums[i])-1
            nums[index]=-abs(nums[index])
        notin=[]
        for x in range(len(nums)):
            if nums[x]>0:
                notin.append(x+1)
        self.arr=notin
        return self.arr
