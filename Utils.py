# get two lines intersection location
def getLineIntersection(l1, l2):
    xdiff = (l1[0][0] - l1[1][0], l2[0][0] - l2[1][0])
    ydiff = (l1[0][1] - l1[1][1], l2[0][1] - l2[1][1])

    def d(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = d(xdiff, ydiff)
    if div == 0:
        return None

    det = (d(*l1), d(*l2))
    x = d(det, xdiff) / div
    y = d(det, ydiff) / div
    return x, y
