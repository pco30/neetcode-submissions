"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(x.start for x in intervals)
        ends = sorted(x.end for x in intervals)
        count = 0
        L = 0

        for start in starts:
            if start < ends[L]:
                count+=1
            else:
                L+=1


        return count
        