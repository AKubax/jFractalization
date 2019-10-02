from numbers_logic import cnumber
import decimal
from numba import cuda
from numba import autojit
from numba import *
import numpy as np
from timeit import default_timer
import random


def reg_iterate(f, z0, n, debug = False):
    res = z0
    for i in range(n):
        res = f(res)
        if debug: print('f^' + str(i + 1) + '(' + str(z0) + ') = ' + str(res))
        if res == cnumber.Infinity: return res

    return res

@jit
def jit_iterate(f, z0, n, debug = False):
    res = z0
    for i in range(n):
        res = f(res)
        if debug: print('f^', i + 1, '(', z0, ') = ', res)
        if res == cnumber.Infinity: return res

    return res

def func(z):
    return z * (z - cnumber(1)) * (z + cnumber(1))

z0 = cnumber(random.random(), random.random())

start = default_timer()
res = reg_iterate(func, z0, 1000)
dt = default_timer() - start
print("Regular exec in %f sec" % dt)

start = default_timer()
res = jit_iterate(func, z0, 1000)
dt = default_timer() - start
print("JIT exec in %f sec" % dt)
