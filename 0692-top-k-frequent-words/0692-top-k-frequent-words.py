class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = Counter(words)
        lst = [(-counter[word],word) for word in counter]
        heapify(lst)
        
        ans = []
        
        for i in range(k):
            ans.append(heappop(lst)[1])
        
        return ans
        