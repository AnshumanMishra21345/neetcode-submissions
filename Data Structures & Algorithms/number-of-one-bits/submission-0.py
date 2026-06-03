class Solution:
    def hammingWeight(self, n: int) -> int:
        ctr=0
        while n>0:
            ctr+=n&1
            n=n>>1
        return ctr

        