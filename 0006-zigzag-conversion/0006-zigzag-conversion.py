class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        word_lst = [[] for _ in range(numRows)]
        to_front = True
        index = 0
        
        for letter in s:
            word_lst[index].append(letter)
            
            if to_front and index + 1 < numRows:
                index += 1
            elif to_front:
                index -= 1
                to_front = False
            elif not to_front and index - 1 >= 0:
                index -= 1
            else:
                to_front = True
                index += 1
        total = []
        for word in word_lst:
            total.extend(word)
        return "".join(total)
        
            
            
        
        