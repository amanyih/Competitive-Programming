class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        res = []
        
        def help(nums,k):
            # print(nums,k)
            if len(nums) == 1:
                res.extend(nums)
                return
            
            less = []
            equal = []
            more = []
            
            pivot = nums[len(nums)//2][0]
            # print("****")
            
            for num in nums:
                if num[0] == pivot:
                    equal.append(num)
                elif num[0] > pivot:
                    more.append(num)
                else:
                    less.append(num)
            # print(less)
            # print(equal)
            # print(more)
            if len(more) > k:
                help(more,k)
            elif len(more) == k:
                res.extend(more)
                return
            elif len(more) + len(equal) == k:
                res.extend(more)
                res.extend(equal)
                return
            else:
                res.extend(more)
                res.extend(equal)
                help(less,k-len(more)-len(equal))
        help([[count[key],key] for key in count],k)
        return [x[1] for x in res]
            
            
            