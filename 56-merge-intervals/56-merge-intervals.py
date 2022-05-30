class Solution(object):
    def merge(self,intervals):
        intervals.sort()
        li=[intervals[0]]
        for x,y in intervals[1:]:
            if x<=li[-1][1]:
                li[-1][1]=max(li[-1][1],y)
            else:
                li.append([x,y])
        return li