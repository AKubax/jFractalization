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

current_zoom = 1
temp_zoom = 0

screen_center = complex(0, 0)
complex_center = complex(0, 0)

leftCorner = complex(-1.5, 1.5)
rightCorner = complex(1.5, -1.5)
density = 100
iterations = 100

scaleX = abs(windowWidth/leftCorner.real)
scaleY = abs(windowHeight/leftCorner.imag)
cornerDelta = rightCorner - leftCorner

def paint_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_fractal(res):
    #global current_zoom
    widthParam = temp_zoom
    heightParam = temp_zoom/windowWidth * windowHeight
    for i in range(0, len(res)):
        for j in range(0, len(res[i])):
            if not math.isnan(res[i][j].real):
                paint_pixel(rescale(i, 0, len(res[i]), widthParam-screen_center.real, windowWidth-widthParam-screen_center.real), rescale(j, 0, len(res), heightParam-screen_center.imag, windowHeight-heightParam-screen_center.imag))
                

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
    global current_zoom
    global temp_zoom

    global screen_center
    global complex_center

    global scaleX
    global scaleY
    global cornerDelta

    tempx = x
    tempy = y
    
    x -= windowWidth/2
    y -= windowHeight/2
    x += screen_center.real
    y += screen_center.imag

    screen_center = complex((screen_center.real+x)/2, (screen_center.imag+y)/2)

    x = tempx
    y = tempy

    x -= windowWidth/2
    y -= windowHeight/2
    
    x *= abs(leftCorner.real - rightCorner.real)/windowWidth
    x += complex_center.real
    y *= abs(leftCorner.imag - rightCorner.imag)/windowHeight
    y += complex_center.imag

    complex_center = complex((complex_center.real+x)/2, -(complex_center.imag+y)/2)

    #deltaX = abs(leftCorner.real - rightCorner.real)
    #deltaY = abs(leftCorner.imag - rightCorner.imag)
    
    
    if out:
        density *= 0.9
        temp_zoom += 50*current_zoom
        current_zoom *= 0.9
    else:
        density *= 1.1
        temp_zoom -= 50*current_zoom
        current_zoom *= 1.1
        
    #deltaX /= (windowWidth-2*temp_zoom)/windowWidth
    #deltaY /= (windowHeight-2*temp_zoom*windowWidth/windowHeight)/windowHeight

    leftCorner = complex((screen_center.real - windowWidth/2)/scaleX * windowWidth/(windowWidth - 2*temp_zoom), -(screen_center.imag - windowHeight/2)/scaleY * windowHeight/(windowHeight-2*(temp_zoom/windowWidth * windowHeight)))
    rightCorner = complex((screen_center.real + windowWidth/2)/scaleX * windowWidth/(windowWidth - 2*temp_zoom), -(screen_center.imag + windowHeight/2)/scaleY * windowHeight/(windowHeight-2*(temp_zoom/windowWidth * windowHeight)))

    
    print()
    print(leftCorner)
    print(rightCorner)
    print()
    
    if temp_zoom <= -500 or temp_zoom >= 50:
        temp_zoom = 0
        screen_center = complex(0, 0)
        complex_center = complex(0, 0)
        res = math_logic.constructIteratedMatrix(math_logic.f, leftCorner, rightCorner, density, iterations)
        print("draw^^^^^")
        
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

    glutMouseWheelFunc(mouseWheelFunc)
    
    #glutMouseFunc(mouseFunc)
    #glutReshapeFunc(resize)
    glutMainLoop()
