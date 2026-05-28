class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D={}
        for i in strs:
            if str(sorted(list(i))) not in D:
                D[str(sorted(list(i)))]=[i]
            else:
                D[str(sorted(list(i)))].append(i)
        return list(D.values())
