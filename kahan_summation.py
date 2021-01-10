from math import fsum


def kahan(l):
    s = 0.000000000
    c = 0.00000000000

    for x in l:
        y = x - c
        t = s + y
        c = (t - s) - y
        s = t
    return s