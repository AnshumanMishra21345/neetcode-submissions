class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals=sorted(intervals,key=lambda k:k.start)
        heap=[]
        for i in intervals:
            #print(heap)
            if heap and heap[0]<=i.start:
                heapq.heappop(heap)
            heapq.heappush(heap,i.end)
        return len(heap)