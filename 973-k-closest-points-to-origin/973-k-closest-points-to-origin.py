class Solution(object):
    def kClosest(self,points, k):
        dis = lambda arg: arg[0] ** 2 + arg[1] ** 2
        points.sort(key= dis)
        return points[:k]