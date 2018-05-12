def intersect(top, bcg, x, y):
    x0, y0 = 0, 0
    x1, y1 = len(bcg[0]), len(bcg)

    x2, y2 = x, y
    x3, y3 = x + len(top[0]), y + len(top)

    x4, y4 = max(x0, x2), max(y0, y2)
    x5, y5 = min(x1, x3), min(y1, y3)

    if x4 >= x5 or y4 >= y5:
        return None

    return x4, y4, x5, y5


def intersect_both(top, bcg, x, y):
    return intersect(bcg, top, -x, -y), intersect(top, bcg, x, y)