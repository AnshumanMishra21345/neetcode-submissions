class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2=0,0
        ctr=0
        for i in range(0,len(num1[::-1])):
            n1+=int(num1[::-1][i])*(10**i)
        for i in range(0,len(num2[::-1])):
            n2+=int(num2[::-1][i])*(10**i)
        return(str(n1*n2))

        