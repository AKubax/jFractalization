from numbers_logic import cnumber
import decimal
from numba import cuda
from numba import autojit
from numba import *
import numpy as np
from timeit import default_timer


decimal.setcontext(decimal.ExtendedContext)

@jit
def iterate(z0, n, debug = False):
    res = z0
    for i in range(n):
        res = F(res)
        if debug: print('f^' + str(i + 1) + '(' + str(z0) + ') = ' + str(res))
        if res == cnumber.Infinity: return res

    return res  

iterate_gpu = cuda.jit(device=True)(iterate)

@cuda.jit
def iterateMatrix_kernel(lowerLeft, upperRight, n, arr):
    width  = arr.shape[0]
    height = arr.shape[1]

    step_x = (upperRight.Re - lowerLeft.Re) / width
    step_y = (upperRight.Im - lowerLeft.Im) / height

    for x in range(width):
        for y in range(height):
            z = cnumber(lowerLeft.Re + x * step_x, lowerLeft.Im + y * step_y)
            arr[x, y] = iterate_gpu(z, n)

arr = np.zeros((1024, 768), dtype = cnumber)
