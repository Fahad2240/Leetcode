class Solution(object):
    def twoSum(self, numbers, target):
        left_=0
        right_=len(numbers)-1
        new=[]
        while left_<=right_:
            if numbers[left_]+numbers[right_]>target:
                right_-=1
            elif numbers[left_]+numbers[right_]<target:
                left_+=1
            else:
                new.append(left_+1)
                new.append(right_+1)
                break         
        return new