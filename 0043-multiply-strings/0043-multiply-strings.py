class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1 = len(num1)
        n2 = len(num2)
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        container = [0] * (n1+n2)
        
        for i in range(n1):
            for j in range(n2):
                
                
                prod = int(num1[i]) * int(num2[j])
                container[i+j] += prod
                container[i+j+1] += container[i+j] //10
                container[i+j] = container[i+j] % 10
                # print(i,j)
                # print(prod)
                # print(container)
                
        while container and container[-1] == 0:
            container.pop()
        container.reverse()
        
        ans = []
        
        for num in container:
            ans.append(str(num))
        
        return "".join(ans)
        
                
        
        