class Solution:
    def isValid(self, s: str) -> bool:
        S=[]
        for i in s:
            if i in "({[":
                S.append(i)
            elif len(S)!=0 and ((i== ")" and S[-1] =="(") or (i== "]" and S[-1] =="[") or (i== "}" and S[-1] =="{")) :
                S.pop()
                print(S)
            else:
                return False
        if len(S)==0:
            return True
        else:
            return False
            