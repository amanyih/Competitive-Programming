/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    var lookup = {}

    for(var i = 0; i < nums.length;i++){
        if(lookup.hasOwnProperty(nums[i])){
            return [lookup[nums[i]],i]
        }
        else{
            lookup[target-nums[i]] = i;
        }
    }
    
};