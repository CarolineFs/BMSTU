def main(x, y, set):
    xa = set[0][0]
    ya = set[0][1]
    xb = set[1][0]
    yb = set[1][1]
    xc = set[2][0]
    yc = set[2][1]
    f = 0
    if ((x - xa) * (ya - yb) - (y - ya) * (xa - xb) > 0):
        if ((x - xb) * (yb - yc) - (y - yb) * (xb - xc) > 0):
            if ((x - xc) * (yc - ya) - (y - ya) * (xc - xa) > 0):
                f = 1

    elif ((x - xa) * (ya - yb) - (y - ya) * (xa - xb) < 0):
        if ((x - xb) * (yb - yc) - (y - yb) * (xb - xc) < 0):
            if ((x - xc) * (yc - ya) - (y - ya) * (xc - xa) < 0):
                f = 1
    elif ((x - xa) * (ya - yb) - (y - ya) * (xa - xb) == 0) \
      or ((x - xb) * (yb - yc) - (y - yb) * (xb - xc) == 0) \
      or ((x - xc) * (yc - ya) - (y - ya) * (xc - xa) == 0):
            f = 2

    return f
