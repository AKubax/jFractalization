from tkinter import*
import random
import math

def paint_pixel(x, y, canvas):
    canvas.create_line(x, y, x+1, y+1, fill='white', width=1)

def draw_fractal(res, canvas):
    for i in range(0, len(res)):
        for j in range(0, len(res[i])):
            if not math.isnan(res[i][j].real):
                paint_pixel(rescale(j, 0, len(res[i]), 0, 600), rescale(i, 0, len(res), 0, 400), canvas)
                

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
    canvas['bg'] = 'black'

    canvas.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
