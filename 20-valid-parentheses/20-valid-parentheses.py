class Solution(object):
    
    def isValid(self,s):
        lst =[]
        for i in range(len(s)):
            if s[i] =="(" or s[i] == "[" or s[i] == "{":
                lst.append(s[i])
            elif len(lst)>0:
                if lst[-1] =="(" and s[i] ==")":
                    lst.pop()
                elif lst[-1] == "[" and s[i] == "]":
                    lst.pop()
                elif lst[-1] == "{" and s[i] == "}":
                    lst.pop()
                else:
                    return False
            else:
                return False
        if len(lst) == 0:
            return True
        else:
            return False