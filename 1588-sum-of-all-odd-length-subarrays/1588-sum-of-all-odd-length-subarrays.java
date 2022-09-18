class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        
        int ans,n;
        ans = 0;
        n = arr.length;
        
        for (int i = 0; i< n;i++){
            int count = ((i+1) * (n-i) +1) / 2;
            ans += count * arr[i];
    
        }
        
        return ans;
        
    }
}