class Solution:
    def countPairs(self, de: List[int]) -> int:
        """
        [2,4,8,16,32]
        
        [1,3,5,7,9]
         l r
         [1,1,1,1]
          0 1 2 3
        """

        possible_scores = [2**i for i in range(1,22)]
        possible_scores.append(1)
        de.sort()
        no_delicious = 0
        for target in possible_scores:
            count = defaultdict(int)
            for num in de:
                subt = target - num
                no_delicious += count[subt]
                count[num] += 1
                
        return no_delicious % (10**9+7)
                        
                    
            
            