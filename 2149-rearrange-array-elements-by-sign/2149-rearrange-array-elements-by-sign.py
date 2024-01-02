class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=0
        neg=1
        new=[None for i in range(len(nums))]
        for item in nums:
            if item>0:
                new[pos]=item
                pos+=2
            else:
                new[neg]=item
                neg+=2
        return new
                
                