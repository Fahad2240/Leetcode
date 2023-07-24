class Solution(object):
    def subarraySum(self, nums, k):
        hashmap={}
        hashmap[0]=1
        count=0
        presum=0
        for item in nums:
            presum+=item
            remove=presum-k
            if remove in hashmap:
                count+=hashmap[remove]
            if presum not in hashmap:
                hashmap[presum]=1
            else:
                hashmap[presum]+=1
        return count
        