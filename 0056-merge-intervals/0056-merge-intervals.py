class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        while i < len(intervals):
            check = False
            if intervals[i][0] <= intervals[i - 1][1] and intervals[i][0] >= intervals[i - 1][0]:
                intervals[i][0] = intervals[i - 1][0]
                check = True
            if intervals[i][1] <= intervals[i - 1][1]:
                intervals[i][1] = intervals[i - 1][1]
                check = True
            if check:
                intervals.remove(intervals[i - 1])
                continue
            i += 1
        return intervals