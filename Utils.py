import numpy as np


# get two lines intersection location
# https://stackoverflow.com/questions/3252194/numpy-and-line-intersections/42727584#42727584
def getLineIntersection(line1, line2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([line1[0], line1[1], line2[0], line2[1]])  # s for stacked
    h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
    l1 = np.cross(h[0], h[1])  # get first line
    l2 = np.cross(h[2], h[3])  # get second line
    x, y, z = np.cross(l1, l2)  # point of intersection

    if z == 0:  # lines are parallel
        return None

    x = round(x/z, 4)
    y = round(y/z, 4)

    if not ((line1[0][0] <= x <= line1[1][0]) or (line1[1][0] <= x <= line1[0][0])):
        return None
    elif not ((line2[0][0] <= x <= line2[1][0]) or (line2[1][0] <= x <= line2[0][0])):
        return None
    elif not ((line1[0][1] <= y <= line1[1][1]) or (line1[1][1] <= y <= line1[0][1])):
        return None
    elif not ((line2[0][1] <= y <= line2[1][1]) or (line2[1][1] <= y <= line2[0][1])):
        return None

    return x, y
