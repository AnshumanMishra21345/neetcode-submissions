class Solution:
    def reverseBits(self, n: int) -> int:
        stri=str(bin(n))[2::][::-1]
        num=int(stri+'0'*(32-len(stri)),2)
        return num



        