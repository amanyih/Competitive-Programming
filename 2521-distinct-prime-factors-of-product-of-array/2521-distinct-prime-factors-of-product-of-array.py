class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        def getAllPrimes(k):
            st = set()
            count = [0] * (k)
            
            
            for i in range(2,k):
                if count[i-1] == 0:
                    count[i-1] += 1
                    st.add(i)
                    for j in range(i,k,i):
                        count[j-1] += 1
            return st
        primes = getAllPrimes(1000)
        lstOfPrimes = set()
        for i in range(len(nums)):
            cur = nums[i]
            for prime in primes:
                if cur % prime == 0:
                    lstOfPrimes.add(prime)
        return len(lstOfPrimes)
            
                        
            
            
        