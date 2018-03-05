"""
extended Euclid’s algorithm
"""


def Euclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, r = Euclid(b, a % b)
        return y, x - (a // b) * y, r


with open("Algorithms\input.txt", "r+") as f:
    strarray = f.read().split()
    a = int(strarray[0])
    b = int(strarray[1])
    (x, y, r) = Euclid(a, b)
    f.write("%d*%d+%d*%d=%d" % (a, x, b, y, r))
