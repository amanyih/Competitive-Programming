class Solution:
    def fizzBuzz(self,n):
        count = 1
        arr = []
        while count <=n:
            if (count % 3 == 0) and (count % 5 == 0):
                arr.append("FizzBuzz")
            elif count % 3 == 0 and count % 5 !=0:
                arr.append("Fizz")
            elif count % 3 !=0 and count % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(count))
            count += 1
        return arr
            
            
            
        