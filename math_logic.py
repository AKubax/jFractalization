import cmath
import math


def iterate(f, z0, n):
    res = z0
    for i in range(n):
        res = f(res)

    return res
    

#density - number of dots per 1 linear unit, n - number of iterations
def constructIteratedMatrix(f, upperLeft, lowerRight, density, n):
    res = []
    re_cntr = 0
    im_cntr = 0

    while re_cntr <= (lowerRight.real - upperLeft.real) * density:
        res.append([])
        while im_cntr <= (upperLeft.imag - lowerRight.imag) * density:
            res[re_cntr].append(iterate(f, complex(upperLeft.real + re_cntr / density, upperLeft.imag - im_cntr / density), n))
            im_cntr += 1

        re_cntr += 1
        im_cntr = 0

    return res


def f(z):
    return z*(z-1)*(z+1)
