class Solution(object):
    def kClosest(self,points, k):
        points.sort(key=lambda arg: arg[0] ** 2 + arg[1] ** 2)
        return points[:k]