class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new=[]
        pos=defaultdict(list)
        it=0
        for num in nums:
            if num not in pos:
                pos[num].append(it)
            else:
                pos[num].append(it)
            it+=1
        nums.sort()
        for num in nums:
            if (target-num) in pos:
                if len(pos[num])==2:
                    new.append(pos[num][0])
                    new.append(pos[num][1])
                    return new
                else:
                    new.append(pos[num][0])
                    new.append(pos[target-num][0])
                    return new
                     