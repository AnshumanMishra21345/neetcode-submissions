class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        ctr=1
        intervals=sorted(intervals,key=lambda k:k.start)
        def between(k,I):
            if k>=I.start and k<I.end:
                return True
            return False
        for i in range(len(intervals)):
            k1,k2=0,0
            for j in range(len(intervals)):
                if between(intervals[i].start,intervals[j]):
                    k1+=1
                if between(intervals[i].end,intervals[j]):
                    k2+=1
            ctr=max(ctr,k1,k2)
        return ctr


        