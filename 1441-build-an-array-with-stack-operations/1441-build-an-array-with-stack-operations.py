class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        ans = []
        l = 0

        for i in range(1,n+2):

            if l < len(target):
                if target[l] == i:
                    ans.append("Push")
                    l+=1
                else:
                    ans.append("Push")
                    ans.append("Pop")
            else:
                return ans

