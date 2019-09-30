#openGL
from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *
from OpenGL.GLUT.freeglut import *
import OpenGL.GLUT.freeglut

#other
import random
import math
import datetime

#:)
import math_logic

windowWidth = 200
windowHeight = 200

complex_center = complex(0, 0)

leftCorner = complex(-1.5, 1.5)
rightCorner = complex(1.5, -1.5)
density = 200
iterations = 100

def paint_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_fractal(res):
    for i in range(0, len(res)):
        for j in range(0, len(res[i])):
            if not math.isnan(res[i][j].real):
                paint_pixel(rescale(i, 0, len(res[i]), 0, windowWidth), rescale(j, 0, len(res), 0, windowHeight))
                

def rescale(value, min_a, max_a, min_b, max_b):
    a = max_a - min_a
    b = max_b - min_b
    value = float(value - min_a)/float(a)
    return min_b + (value * b)


def create_window():
    pass

def iterate():
    glViewport(0, 0, windowWidth, windowHeight)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, windowWidth, windowHeight, 0.0, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def show_fractal():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    draw_fractal(res)
    glutSwapBuffers()
    print(datetime.datetime.now())

def show_screen():
    pass

'''
def resize(width, height):
    glutReshapeWindow(windowWidth, windowHeight)
    show_fractal()
    
'''

'''
def mouseFunc(button, state, x, y):
    print(button, " ", state, " ", x, " ", y)
    
'''

def zoom(x, y, out):
    global leftCorner
    global rightCorner
    global res
    global density
    global complex_center

    x -= windowWidth/2
    y -= windowHeight/2

    if out:
        density *= 0.8
        x *= -1
    else:
        density *= 1.2
        y *= -1

    x *= abs(leftCorner.real - rightCorner.real)/windowWidth
    y *= abs(leftCorner.imag - rightCorner.imag)/windowHeight
    
    x += complex_center.real
    y += complex_center.imag
    
    complex_center = complex((complex_center.real + x)/2, (complex_center.imag + y)/2)
    print(density)
    leftCorner = complex(complex_center.real - windowWidth/(2*density), complex_center.imag + windowHeight/(2*density))
    rightCorner = complex(complex_center.real + windowWidth/(2*density), complex_center.imag - windowHeight/(2*density))

    res = math_logic.constructIteratedMatrix(math_logic.f, leftCorner, rightCorner, density, iterations)
        
    show_fractal()
    
def keyboardFunc(key, x, y):    
    if key == b'e':
        zoom(x, y, False)
    elif key == b'q':
        zoom(x, y, True)
    print(key)

def mouseWheelFunc(button, direction, x, y):
    if direction == -1:
        zoom(x, y, True)
    else:
        zoom(x, y, False)

if __name__ == "__main__":
    print(datetime.datetime.now())
    res = math_logic.constructIteratedMatrix(math_logic.f, leftCorner, rightCorner, density, iterations)
    print(datetime.datetime.now())
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
    glutInitWindowSize(windowWidth, windowHeight)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"jFractalization")

    glutDisplayFunc(show_fractal)
    glutIdleFunc(show_screen)

    glutKeyboardFunc(keyboardFunc)
    glutMouseWheelFunc(mouseWheelFunc)
    
    #glutMouseFunc(mouseFunc)
    #glutReshapeFunc(resize)
    glutMainLoop()
