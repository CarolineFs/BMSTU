def main(x, y):
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
