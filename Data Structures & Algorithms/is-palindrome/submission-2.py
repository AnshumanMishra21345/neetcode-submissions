import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if i in set(string.ascii_letters+string.digits):
                st+=i
        l=0
        r=len(st)-1
        print(st)
        while l<r: 
            print(st[l],st[r],'checkpal')
            if st[l].upper()!=st[r].upper():
                return False
            l+=1
            r-=1
        return True
        