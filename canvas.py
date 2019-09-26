from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *

import random
import math


def paint_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


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


def create_window():
    pass

def iterate():
    glViewport(0, 0, 500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    paint_pixel(100, 100)
    glutSwapBuffers()

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
    glutInitWindowSize(600, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"jFractalization")

    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMainLoop()
