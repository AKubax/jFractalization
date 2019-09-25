from tkinter import*
import random

def paint_pixel(x, y, canvas):
    canvas.create_line(x, y, x+1, y+1, fill='white', width=1)

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
