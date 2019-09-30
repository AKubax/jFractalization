import numbers_logic
import decimal
from threading import Thread

import pandas
import seaborn
import matplotlib


decimal.setcontext(decimal.ExtendedContext)

def iterate(f, z0, n):
    res = z0
    for i in range(n):
        res = f(res)

    return res
   
class IteratorThread(Thread):

    def __init__(self, f, z, n, i, j):
        Thread.__init__(self)
        self.name = str(z)
        self.f = f
        self.z = z
        self.n = n
        self.i = i
        self.j = j

    def run(self):
        global ITERATED_MATRIX

        print("(%d, %d)" % (self.i, self.j))
        ITERATED_MATRIX[self.i][self.j] = iterate(self.f, self.z, self.n)
        
ITERATED_MATRIX = {}

#density - number of dots per 1 linear unit, n - number of iterations
def constructIteratedMatrix(f, upperLeft, lowerRight, density, n):
    global ITERATED_MATRIX
    
    ITERATED_MATRIX = {i : {j : numbers_logic.cnumber.NaN for j in range(1 + int((upperLeft.Im - lowerRight.Im) * density))} for i in range(1 + int((lowerRight.Re - upperLeft.Re) * density))}
    re_cntr = decimal.Decimal(0)
    im_cntr = decimal.Decimal(0)
    density = decimal.Decimal(density)

    while re_cntr <= (lowerRight.Re - upperLeft.Re) * density:
        while im_cntr <= (upperLeft.Im - lowerRight.Im) * density:
            IteratorThread(f, numbers_logic.cnumber(upperLeft.Re + re_cntr / density, upperLeft.Im - im_cntr / density), n, int(re_cntr), int(im_cntr)).start()
            im_cntr += 1

        re_cntr += 1
        im_cntr = 0
        

#primitive plotting:
            
def heatmapIteratedMatrix(mat, upperLeft, lowerRight, density):
    modMat = []
    for i in range(len(mat)):
        modMat.append([])
        for j in range(len(mat[i])):
            modMat[i].append(abs(mat[i][j]))
        
    seaborn.heatmap(pandas.DataFrame(modMat, index = [upperLeft.Im - decimal.Decimal(i) / decimal.Decimal(density) for i in range(int((upperLeft.Im - lowerRight.Im) * density) + 1)], columns = [upperLeft.Re + float(i) / density for i in range(int((upperLeft.Im - lowerRight.Im) * density) + 1)]))
    matplotlib.pyplot.show()

def func(z):
	return z * (z - numbers_logic.cnumber(1)) * (z + numbers_logic.cnumber(1))

constructIteratedMatrix(func, numbers_logic.cnumber(-1, 1), numbers_logic.cnumber(1, -1), 5, 100)
#heatmapIteratedMatrix(ITERATED_MATRIX, numbers_logic.cnumber(-1, 1), numbers_logic.cnumber(1, -1), 5)

