class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict_ ={}
        
        for item in items1:
            dict_[item[0]] = item[1]
        
        for item in items2:
            if item[0] in dict_:
                dict_[item[0]] += item[1]
            else:
                dict_[item[0]] = item[1]
        
        return [[x,dict_[x]] for x in sorted(dict_)]