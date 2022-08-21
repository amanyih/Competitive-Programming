class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        _dict = {}

        for num in arr:
            if _dict and num in _dict:
                _dict[num] += 1
            else:
                _dict[num] = 1
        count = 0
        ans =[]
        for key, value in sorted(_dict.items(),key = lambda kv:(kv[1],kv[0]), reverse= True):
            if count>= len(arr)/2:
                break
            else:
                ans.append(key)
                count += value
        return len(ans)