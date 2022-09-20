class NumArray {
    int[] nums;
    int[] prefixSum;

    public NumArray(int[] nums) {
        this.nums = nums;
        int prefix = 0;
        int[] prefixSumm = new int[nums.length];
        for (int i = 0; i < nums.length;i++){
            prefix += nums[i];
            prefixSumm[i] = prefix;
        }
        this.prefixSum = prefixSumm;
        
    }
    
    public int sumRange(int left, int right) {
        
        return this.prefixSum[right] - this.prefixSum[left] + this.nums[left];
        
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */