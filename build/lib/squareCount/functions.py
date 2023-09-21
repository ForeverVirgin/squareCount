import math
from decimal import Decimal

def count_square(param):
    if type(param) == type(10):
        return count_circle_square(param)
    elif type(param) == type([1,2,3]):
        if len(param) == 3:
            return count_triangle_square(param[0],param[1],param[2])
        else:
            return TypeError
    else:
        return TypeError


def count_circle_square(radius):
    dec_radius = Decimal(str(radius))
    return dec_radius * dec_radius * Decimal(str(math.pi)).quantize(Decimal("1.000"))

def count_triangle_square(a, b, c):
    if(a+b>c and a+c>b and b+c>a):
        if (not isRectangular(a, b, c)):
            p = (a + b + c) / 2
            return math.sqrt(p * (p - a) * (p - b) * (p - c))
        else:
            c1, c2 = isRectangular(a, b, c)
            return c1 * c2 / 2
    else:
        return "Impossible triangle"

def isRectangular(a, b, c):
    if a**2 + b**2 == c**2:
        return a, b
    elif a**2 + c**2 == b**2:
        return a, c
    elif b**2 + c**2 == a**2:
        return b, c
    else:
        return False
