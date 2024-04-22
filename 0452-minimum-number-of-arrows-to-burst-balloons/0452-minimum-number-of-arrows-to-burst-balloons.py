class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        counter = 1
        i = 0
        x = points[0][0]
        y = points[0][1]
        while i < len(points):
            if points[i][0] > y:
                x = points[i][0]
                y = points[i][1]
                counter += 1
            y = min(points[i][1], y)
            x = max(points[i][0], x)
            i += 1
        return(counter)