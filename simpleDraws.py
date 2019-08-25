import pygame
from pygame.locals import *
from OpenGL.GL import *


def draw(i):
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    if i == 1:
        draw1(1)
        draw1(2)
    if i == 2:
        draw2(1)
        draw2(2)
    if i == 3:
        draw3(1)
        draw3(2)
    if i == 4:
        draw4(1)
        draw4(2)
    if i == 5:
        draw5(1)
        draw5(2)
    if i == 6:
        draw6(1)
        draw6(2)
    if i == 7:
        draw7(1)
        draw7(2)
    if i == 8:
        draw8(1)
        draw8(2)
    if i == 9:
        draw9(1)
        draw9(2)
    if i == 10:
        draw10()
    if i == 11:
        draw11()


def draw1(i):
    if i == 1:
        glColor3ub(200, 200, 255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glColor3ub(0, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(50, 50)
    glVertex2f(25, 25)
    glVertex2f(50, -50)
    glVertex2f(25, -25)
    glVertex2f(-50, -50)
    glVertex2f(-25, -25)
    glVertex2f(-50, 50)
    glVertex2f(-25, 25)
    glVertex2f(50, 50)
    glVertex2f(25, 25)
    glEnd()


def draw2(i):
    if i == 1:
        glColor3ub(200, 200, 255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glColor3ub(0, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(50, 35)
    glVertex2f(50, 50)
    glVertex2f(35, 35)
    glVertex2f(20, 50)
    glVertex2f(35, -25)
    glVertex2f(20, -10)
    glVertex2f(15, -25)
    glVertex2f(10, -10)
    glVertex2f(-5, -25)
    glVertex2f(10, 50)
    glVertex2f(-5, 35)
    glVertex2f(-20, 50)
    glVertex2f(-20, 35)
    glEnd()


def draw3(i):
    if i == 1:
        glColor3ub(200, 200, 255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glColor3ub(0, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(50, -50)
    glVertex2f(25.38, 11.54)
    glVertex2f(50, 30)
    glVertex2f(-50, -45)
    glVertex2f(10, 50)
    glEnd()


def draw4(i):
    if i == 1:
        glColor3ub(200, 200, 255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glColor3ub(0, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(50, 30)
    glVertex2f(30, 50)
    glVertex2f(0, 20)
    glVertex2f(-20, 40)
    glVertex2f(0, -50)
    glVertex2f(-20, -30)
    glEnd()


def draw5(i):
    if i == 1:
        glColor3ub(200, 200, 255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glColor3ub(0, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(50, -50)
    glVertex2f(-30, -50)
    glVertex2f(-10, -20)
    glVertex2f(-25, 50)
    glEnd()


def draw6(i):
    if i == 1:
        glColor3ub(200, 200, 255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glColor3ub(0, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(-25, 55)
    glVertex2f(-50, -50)
    glVertex2f(-15, -15)
    glVertex2f(25, -35)
    glVertex2f(40, 50)
    glEnd()


def draw7(i):
    if i == 1:
        glColor3ub(200, 200, 255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glColor3ub(0, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(-50, -70)
    glVertex2f(50, -70)
    glVertex2f(-50, 70)
    glVertex2f(50, 70)
    glEnd()


def draw8(i):
    if i == 1:
        glColor3ub(200, 200, 255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glColor3ub(0, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(40, -10)
    glVertex2f(20, 50)
    glVertex2f(0, -50)
    glVertex2f(-40, 30)
    glEnd()


def draw9(i):
    if i == 1:
        glColor3ub(200, 200, 255)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glColor3ub(0, 0, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-30, -20)
    glVertex2f(-25, 20)
    glVertex2f(0, 50)
    glVertex2f(50, 30)
    glVertex2f(40, -30)
    glVertex2f(-10, -50)
    glEnd()


def draw10():
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3ub(226, 73, 66)
    glBegin(GL_POLYGON)
    glVertex2f(50, 50)
    glVertex2f(50, -50)
    glVertex2f(-50, -50)
    glVertex2f(-50, 50)
    glEnd()

    glColor3ub(123, 181, 70)
    glBegin(GL_POLYGON)
    glVertex2f(16.6, 16.6)
    glVertex2f(16.6, -16.6)
    glVertex2f(-16.6, -16.6)
    glVertex2f(-16.6, 16.6)
    glEnd()


def draw11():
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 255)
    glVertex2f(50, 50)
    glColor3ub(0, 255, 0)
    glVertex2f(50, -50)
    glColor3ub(255, 0, 0)
    glVertex2f(-50, -50)
    glColor3ub(255, 255, 0)
    glVertex2f(-50, 50)
    glEnd()


def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_caption('Trabalho 1')
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(-100, 100, -100, 100, -10, 10)
    max = 11
    i = 1
    draw(i)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if i < max:
                        i = i + 1
                    else:
                        i = 1
                    draw(i)
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if i > 1:
                        i = i - 1
                    else:
                        i = max
                    draw(i)
                    pygame.display.flip()


main()
