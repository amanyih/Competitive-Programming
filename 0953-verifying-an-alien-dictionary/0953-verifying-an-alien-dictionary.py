class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        _dict = {}
        for i,char in enumerate(order):
            _dict[char] = i
        word_as_num = []
        for word in words:
            string = ""
            for char in word:
                string += str(_dict[char])
                string += "-"
            newList = string.split("-")
            newList.pop()
            for j in range(len(newList)):
                newList[j] = int(newList[j])
            word_as_num.append(newList)
        for i in range(1,len(word_as_num)):
            if word_as_num[i]< word_as_num[i-1]:
                return False
        
        return True
                
            
        
            
        