class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash={}
        for item in nums:
            # temp.add(item)
            if item not in hash:
                hash[item]=True
        longest=-1000000001
        for item in nums:
            if item-1 not in hash:
                cons_element=1
                while item+1 in hash:
                    cons_element+=1
                    item+=1
                longest=max(longest,cons_element)
        if len(nums)==0:
            return 0
        return longest