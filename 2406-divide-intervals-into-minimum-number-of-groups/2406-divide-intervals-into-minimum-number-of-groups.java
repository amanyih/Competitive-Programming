class Solution {
    public int minGroups(int[][] intervals) {
        
        int maxInt = intervals[0][1];
        
        for (int[] interval:intervals){
            if(interval[1] > maxInt){
                maxInt = interval[1];
            }
        }
        int[] prefix = new int[maxInt+2];
        for (int[] interval:intervals){
            prefix[interval[0]] ++;
            prefix[interval[1]+1] --;
        }
        int ans = 0;
        for (int i = 1; i < prefix.length; i++){
            prefix[i] = prefix[i-1]+prefix[i];
            
            if (prefix[i] > ans){
                ans = prefix[i];
            }
        }
        
        return ans;
        
    }
}