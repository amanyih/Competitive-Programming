class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        
        
        maxpos = 0
        
        for fruit in fruits:
            maxpos = max(maxpos,fruit[0])
        maxpos = max(maxpos+1,startPos+k)
        arr = [0] * (maxpos + 2)
        
        for fruit in fruits:
            pos,amount = fruit
            arr[pos] += amount
        prefix = list(accumulate(arr))
        
        ans = 0
        # print(arr)
        # print(prefix)
        for i in range(startPos-k,startPos+k+1):
            if (i < startPos and startPos - i == k):
                cur = prefix[startPos] - (prefix[i - 1] if i - 1 >= 0 else 0)
                # print("1",cur)
            elif i < startPos and (startPos - i) * 2 < k:
                # print("iii")
                right = startPos + (k-(startPos-i)*2)
                cur = prefix[right] - (prefix[i - 1] if i - 1 >= 0 else 0)
                # print("2",cur)
            elif i < startPos:
                cur = prefix[startPos] - (prefix[i - 1] if i - 1 >= 0 else 0)
                # print("3",cur)
            elif i == startPos:
                cur = prefix[startPos+k] - (prefix[i - 1] if i - 1 >= 0 else 0)
                # print("4",cur)
            elif (i - startPos ) * 2 < k:
                # print("i",i,"startPos",startPos)
                left = startPos - (k-(i-startPos)*2)
                # print("left",left)
                cur = prefix[i] - (prefix[left - 1] if left - 1 >= 0 else 0)
                # print("5",cur)
            else:
                cur = prefix[i] - (prefix[startPos - 1] if startPos - 1 >= 0 else 0)
                # print("6",cur)
            ans = max(cur,ans)
            # print(ans,i)

        return ans
            
            
        