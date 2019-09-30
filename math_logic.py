from numbers_logic import cnumber
import decimal
from threading import Thread


decimal.setcontext(decimal.ExtendedContext)

def iterate(f, z0, n, debug = False):
    res = z0
    for i in range(n):
        res = f(res)
        if debug: print('f^' + str(i + 1) + '(' + str(z0) + ') = ' + str(res))
        if res == cnumber.Infinity: return res

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
        ITERATED_MATRIX[self.i][self.j] = iterate(self.f, self.z, self.n)
        
ITERATED_MATRIX = {}

#density - number of dots per 1 linear unit, n - number of iterations
def constructIteratedMatrix(f, upperLeft, lowerRight, density, n):
    global ITERATED_MATRIX

    print('pajalusta!!!')
    ITERATED_MATRIX = {i : {j : cnumber.NaN for j in range(1 + int((upperLeft.Im - lowerRight.Im) * density))} for i in range(1 + int((lowerRight.Re - upperLeft.Re) * density))}
    #print(ITERATED_MATRIX)
    re_cntr = decimal.Decimal(0)
    im_cntr = decimal.Decimal(0)
    density = decimal.Decimal(density)

    p = []

    while re_cntr <= (lowerRight.Re - upperLeft.Re) * density:
        while im_cntr <= (upperLeft.Im - lowerRight.Im) * density:
            p.append(IteratorThread(f, cnumber(upperLeft.Re + re_cntr / density, upperLeft.Im - im_cntr / density), n, int(re_cntr), int(im_cntr)))
            im_cntr += 1

        re_cntr += 1
        im_cntr = 0
        
    for el in p: el.start()
    for el in p: el.join()
    print('sbasiba!!!!!')


constructIteratedMatrix(lambda z: z * z, cnumber(-1, 1), cnumber(1, -1), 300, 100)
#heatmapIteratedMatrix(ITERATED_MATRIX, cnumber(-1, 1), cnumber(1, -1), 5)

