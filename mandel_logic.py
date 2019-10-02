from numba import cuda
from numba import autojit
from numba import *
import numpy as np
from timeit import default_timer as timer
from numbers_logic import cnumber


blockdim = (32, 32)
griddim  = (32, 32)



@jit
def mandel_iterate(re, im, n, crit, debug = False):
    c = complex(re, im)
    z = complex(0, 0)
    for i in range(n):
        z = z*z + c
        if z.real**2 + z.imag**2 > crit**2: return i

    return n

iterate_gpu = cuda.jit(device=True)(mandel_iterate)

@cuda.jit
def iterateMatrix_kernel(minX, minY, maxX, maxY, n, crit, arr):
    width  = arr.shape[0]
    height = arr.shape[1]

    step_x = (maxX - minX) / width
    step_y = (maxY - minY) / height

    gpu_x, gpu_y = cuda.grid(2)
    grid_width = cuda.gridDim.x * cuda.blockDim.x
    grid_height = cuda.gridDim.y * cuda.blockDim.y

    for x in range(gpu_x, width, grid_width):
        for y in range(gpu_y, height, grid_height):
            re = minX + x * step_x
            im = minY + y * step_y
            arr[x, y] = iterate_gpu(re, im, n, crit, False)

def constructIteratedMatrix(lowerLeft, upperRight, density, n, crit, debug = False):
    arr = np.zeros(( int((upperRight.Re - lowerLeft.Re) * density), int((upperRight.Im - lowerLeft.Im) * density) ), dtype = np.uint8)
    start = timer()
    d_image = cuda.to_device(arr)
    iterateMatrix_kernel[griddim, blockdim](float(lowerLeft.Re), float(lowerLeft.Im), float(upperRight.Re), float(upperRight.Im), n, crit, arr)
    d_image.to_host()
    dt = timer() - start

    if debug: print("Matrix has been constructed in %f sec" % dt)
    return arr


#first false call to shorten the duration next time
arr = np.zeros((1, 1), dtype = np.uint8)
d_image = cuda.to_device(arr)
iterateMatrix_kernel[griddim, blockdim](-1.0, -1.0, 1.0, 1.0, 1, 1, d_image) 
d_image.to_host()


'''
width  = 1000
height = 1000

n = 100
crit = 10




arr = np.zeros((width, height), dtype = np.uint8)
start = timer()
d_image = cuda.to_device(arr)
iterateMatrix_kernel[griddim, blockdim](-1.0, -1.0, 1.0, 1.0, n, crit, d_image) 
d_image.to_host()
dt = timer() - start
'''
