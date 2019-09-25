from tkinter import*
import random
import math

def paint_pixel(x, y, canvas):
    canvas.create_line(x, y, x+1, y+1, fill='white', width=1)

def draw_fractal(res, canvas):
    for i in range(0, len(res)):
        for j in range(0, len(res[i])):
            if not math.isnan(res[i][j].real):
                paint_pixel(rescale(i, 0, len(res[i]), 0, 600), rescale(j, 0, len(res[i]), 0, 400), canvas)
                
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
    canvas = Canvas(root, width=600, height=400, bg='white')
    canvas['bg'] = 'black'
    
    Button(text="rand", width=20, command=lambda: paint_pixel(random.randint(0, 600), random.randint(0, 400), canvas)).pack()
    canvas.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
