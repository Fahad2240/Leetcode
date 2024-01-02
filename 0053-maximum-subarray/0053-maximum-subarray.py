class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_glob=max_c=nums[0]
        for x in range(1,len(nums)):
            max_c=max(nums[x],max_c+nums[x])
            if max_c>max_glob:
                max_glob=max_c
        return max_glob