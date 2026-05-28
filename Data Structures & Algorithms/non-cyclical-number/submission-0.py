class Solution:
    def isHappy(self, n: int) -> bool:
        ctr=[]
        k=n
        while 1:
            if self.check(k)==1:
                return True
                break
            else:
                if self.check(k) in ctr:
                    return False
                    break
                ctr.append(self.check(k))
            #print(k,ctr)
            k=self.check(k)
            
        
    def check(self,n):
        i=n
        nums=[]
        while i!=0:
            nums.append(i%10)
            i=i//10
        su=sum([i**2 for i in nums])
        if su==1:
            return True
        else:
            return su