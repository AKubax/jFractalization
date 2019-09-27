from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *

import random
import math

windowWidth = 640
windowHeight = 480

def paint_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_fractal(res):
    for i in range(0, len(res)):
        for j in range(0, len(res[i])):
            if not math.isnan(res[i][j].real):
                paint_pixel(rescale(j, 0, len(res[i]), 0, windowWidth), rescale(i, 0, len(res), 0, windowHeight))
                

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

def showScreen(res = 0):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    if res != 0:
        draw_fractal(res)
    glutSwapBuffers()

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
    glutInitWindowSize(windowWidth, windowHeight)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"jFractalization")

    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen(res))
    glutMainLoop()
