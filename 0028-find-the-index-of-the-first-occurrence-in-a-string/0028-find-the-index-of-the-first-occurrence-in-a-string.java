class Solution {
    public int strStr(String haystack, String needle) {

        for(int i = 0; i < haystack.length();i++){
            if (i+needle.length() <= haystack.length()){
                if(needle.equals(haystack.substring(i,i+needle.length()))){
                return i;
            }
            }
            else{
                if(needle.equals(haystack.substring(i,haystack.length()))){
                    return i;
                }
            }
            
        }
        return -1;
        
    }
}