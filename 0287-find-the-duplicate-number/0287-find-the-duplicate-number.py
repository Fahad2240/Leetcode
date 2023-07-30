class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p=0
        nums.sort()
        for item in nums:
            if item==p:
                return p
            p=item