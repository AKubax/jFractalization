from tkinter import*
import random
import math

def iterate(f, z0, n):
    res = z0
    for i in range(n):
        res = f(res)
        if math.isnan(res.real):
            return i
        
    return n
    

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

def paint_pixel(x, y, color, canvas):
    canvas.create_line(x, y, x+1, y+1, fill= '#%02x%02x%02x' % color, width=1)

def draw_fractal(res, canvas):
    for i in range(0, len(res)):
        for j in range(0, len(res[i])):
            color = int(rescale(res[i][j], 0, 50, 0, 256))
            paint_pixel(rescale(i, 0, len(res[i]), 0, 600), rescale(j, 0, len(res), 0, 400), (color, color, color), canvas)
                
def f(z):
    return z*z + complex(-0.8 , 0.156)

def rescale(value, min_a, max_a, min_b, max_b):
    a = max_a - min_a
    b = max_b - min_b
    value = float(value - min_a)/float(a)
    return min_b + (value * b)

def main():
    root = Tk()
    root.geometry('600x400+0+0')
    root.title("jFractalization")
    root['bg'] = 'white'
    root.resizable(False, False)
    
    canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='white')
    canvas['bg'] = 'white'

    res = constructIteratedMatrix(f, complex(-1.5, 1.5), complex(1.5, -1.5), 300, 50)
    draw_fractal(res, canvas)

    canvas.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
