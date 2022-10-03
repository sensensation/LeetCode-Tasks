#1779. Find Nearest Point That Has the Same X or Y Coordinate
# You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
# You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
# A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.
# Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
# If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.
# The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
def nearestValidPoint(x: int, y: int, points) -> int:
    res = float("inf")
    idx = -1
    for i, point in enumerate(points):
        if (x == point[0] or y == point[1]):
            dist = abs(point[0] - x) + abs(point[1] - y)
            if (dist < res):
                res = dist
                idx = i
                
    return print(idx)

nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]])


