class Solution {
    public int[] runningSum(int[] nums) {
        
        int prefix = 0;
        int[] prefixSum = new int[nums.length];
        
        for (int i = 0; i< nums.length; i++){
            prefix += nums[i];
            prefixSum[i] = prefix;
        }
        
        return prefixSum;
    }
}