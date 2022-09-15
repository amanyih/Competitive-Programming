class Solution:
    def minimumBuckets(self, street: str) -> int:
        if street[0] == "H" and len(street) == 1:
            return -1
        indices = set()
        
        for index in range(len(street)):
            if index == 0:
                if street[index] == ".":
                    continue
                if street[index] == "H" and street[index + 1] == ".":
                    indices.add(index+1)
                else:
                    return -1
            elif index == len(street) -1:
                if street[index] == "H":
                    if street[index-1] == "H":
                        return -1
                    elif street[index -1] == "." and (index - 1) in indices:
                        continue
                    else:
                        indices.add(index-1)
            elif street[index] == "H":
                if street[index-1] =="." and (index - 1) in indices:
                    continue
                elif street[index + 1] == ".":
                    indices.add(index+1)
                elif street[index-1] == ".":
                    indices.add(index-1)
                else:
                    return -1
        
        return len(indices)
                    
                
                 
        