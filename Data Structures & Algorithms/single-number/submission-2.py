class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ctr=0
        for i in nums:
            ctr^=i
        return ctr