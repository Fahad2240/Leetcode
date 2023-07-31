class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        new=[]
        make=set()
        hash={}
        nums.sort()
        for item in nums:
            make.add(item)
            if item not in hash:
                hash[item]=1
            else:
                hash[item]+=1
        for item in make:
            if hash[item]>(int)(len(nums)/3):
                new.append(item)
        return new