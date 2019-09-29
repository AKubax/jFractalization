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

windowWidth = 640
windowHeight = 480

temp_zoom = 0
current_scale = 1

screen_center = complex(0, 0)
complex_center = complex(0, 0)

leftCorner = complex(-1.5, 1.5)
rightCorner = complex(1.5, -1.5)
lreal = leftCorner.real
density = 10
iterations = 100

scaleX = abs(windowWidth/abs(leftCorner.real - rightCorner.real))
scaleY = abs(windowHeight/abs(leftCorner.imag - rightCorner.imag))
cornerDelta = rightCorner - leftCorner


def paint_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_fractal(res):
    #global current_zoom
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
    global temp_zoom
    global lreal
    global current_scale

    lreal = abs(lreal)

    if out:
        current_scale /= 0.9
    else:
        current_scale *= 0.9

    widthParam = (leftCorner.real + rightCorner.real)/2
    heightParam = (leftCorner.imag + rightCorner.imag)/2
    leftCorner = complex(widthParam - lreal*current_scale, heightParam + lreal*current_scale)
    rightCorner = complex(widthParam + lreal*current_scale, heightParam - lreal*current_scale)
    
    if temp_zoom <= -500 or temp_zoom >= 50 or True:
        temp_zoom = 0
        res = math_logic.constructIteratedMatrix(math_logic.f, leftCorner, rightCorner, density, iterations)
        
    show_fractal()
    
def keyboardFunc(key, x, y):
    global leftCorner
    global rightCorner
    global res
    global current_scale
    #current_scale = abs(leftCorner.real/lreal)
    
    if key == b'w':
        leftCorner = complex(leftCorner.real, leftCorner.imag + 0.1*current_scale)
        rightCorner = complex(rightCorner.real, rightCorner.imag + 0.1*current_scale)
    elif key == b's':
        leftCorner = complex(leftCorner.real, leftCorner.imag - 0.1*current_scale)
        rightCorner = complex(rightCorner.real, rightCorner.imag - 0.1*current_scale)
    elif key == b'a':
        leftCorner = complex(leftCorner.real - 0.1*current_scale, leftCorner.imag)
        rightCorner = complex(rightCorner.real - 0.1*current_scale, rightCorner.imag)
    elif key == b'd':
        leftCorner = complex(leftCorner.real + 0.1*current_scale, leftCorner.imag)
        rightCorner = complex(rightCorner.real + 0.1*current_scale, rightCorner.imag)
    print(key)
    res = math_logic.constructIteratedMatrix(math_logic.f, leftCorner, rightCorner, density, iterations)
    show_fractal()

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
