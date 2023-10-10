class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        v4 = queryIP.split(".")
        v6 = queryIP.split(":")
        if len(v4) == 4:
            v4s = []
            for ip in v4:
                if not(0 < len(ip) <= 3):
                    return "Neither"
                isValid = True
                for char in ip:
                    if not (0 <=ord(char) - ord("0") <=9):
                        return "Neither"
                if len(ip) != len(str(int(ip))) or not (0 <=int(ip)<= 255):
                    return "Neither"
                if isValid:
                    v4s.append(ip)
                else:
                    return "Neither"
            return "IPv4"
        elif len(v6) == 8:
            v6s = []

            for ip in v6:
                if not (0< len(ip) <= 4):
                    # print("here")
                    return "Neither"
                isValid = True
                for char in ip:
                    if  not (0 <=ord(char) - ord("0") <=10) and not(0 <=ord(char) - ord("a") <=5) and not(0 <=ord(char) - ord("A") <=5):
                        # print(char)
                        return "Neither"

            return "IPv6"
        return "Neither"
                
        
                    
                
            
        
        