class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        new=[]
        new.append(intervals[0])
        for x in range(1,len(intervals)):
            if intervals[x][0]<=new[len(new)-1][1]:
                if intervals[x][1]>new[len(new)-1][1]:
                    new[len(new)-1][1]=intervals[x][1]
            else:
                new.append(intervals[x])
        return new