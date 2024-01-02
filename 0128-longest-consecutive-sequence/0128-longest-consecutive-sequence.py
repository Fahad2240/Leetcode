class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set=set(nums)
        longest_cons=0
        for elem in nums:
            if elem-1 not in new_set:
                c_elem=elem
                c_len=1
                while c_elem+1 in new_set:
                    c_elem+=1
                    c_len+=1
                longest_cons=max(c_len,longest_cons)
        return longest_cons
        # print(new_set)
        # return 1