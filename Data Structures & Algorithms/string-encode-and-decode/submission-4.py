class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "-"
        if len(strs)==1:
            return strs[0]
        r_st=""
        for i in strs[:-1]:
            r_st+=i+"$#@"
        r_st+=strs[-1]
        return r_st


    def decode(self, s: str) -> List[str]:
        if s is "-":
            return []
        if "$#@" not in s:
            return [s]
        return s.split("$#@")
