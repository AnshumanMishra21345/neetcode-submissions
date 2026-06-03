class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(s.split())
        if sorted([i for i in s]) == sorted([i for i in t]):
            return True
        return False
        