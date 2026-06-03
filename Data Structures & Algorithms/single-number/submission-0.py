class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ctr=set()
        for i in nums:
            if i in ctr:
                ctr.remove(i)
            else:
                ctr.add(i)
            print(ctr)
        return int(*ctr)