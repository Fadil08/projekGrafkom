import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

os.system('cls')
w,h= 500,500

play = False
crashObstacle = False
xPosition = 0
yPosition = 0

#=== draw text ================================================================================

def drawText(ch,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))    
 
def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = (0,0,0)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  


#=== Colors =================================================================================
x_r_player1 = random.randrange(150,250,10)

black = 0,0,0
lightcream = 247,209,183
cream = 211,133,101
brown = 77,60,56
lightbrown = 101,80,75
maroon = 108,37,65
brick = 194,67,62
lightgrey = 42,51,55
grey = 30,37,42

def scorebord():
    glBegin(GL_POLYGON) 
    glColor3ub(101,80,75)
    glVertex2f(-1000,-930) 
    glVertex2f(-1000,-1000) 
    glVertex2f(1000,-1000) 
    glVertex2f(1000,-930) 
    glEnd()

def kotak(x,y,height,width,color):
    glBegin(GL_POLYGON) 
    glColor3ub(color[0],color[1],color[2])
    glVertex2f((x-900),(y-600)) # pojok kiri atas
    glVertex2f((x-900), ((y-600) - height))
    glVertex2f(((x-900) + width), ((y-600) - height))
    glVertex2f(((x-900) + width), (y-600))
    glEnd()

def char1():    # Main Character
    glTranslated(xPosition, yPosition, 0)

    kotak(0,4,4,17,lightcream)
    kotak(-4,19,15,21,lightcream)
    kotak(17,10,6,5,lightcream)
    kotak(-25,19,5,5,lightcream)
    kotak(16,-12,5,5,lightcream)
    kotak(-8,44,21,36,lightbrown)
    kotak(-14,28,28,10,cream)
    kotak(-4,28,9,4,cream)
    kotak(-4,4,4,4,cream)
    kotak(0,23,4,22,cream)
    kotak(-20,10,6,6,cream)
    kotak(-25,15,5,11,cream)
    kotak(-25,40,21,11,brown)
    kotak(-20,19,4,6,brown)
    kotak(-20,44,16,12,brown)
    kotak(-8,35,7,8,brown)
    kotak(0,28,5,7,brown)
    kotak(-25,0,13,37,maroon)
    kotak(-15,-12,5,11,maroon)
    kotak(-25,-12,5,5,cream)
    kotak(-4,-12,5,16,brick)
    kotak(-4,-17,5,16,lightgrey)
    kotak(6,-22,5,6,lightgrey)
    kotak(-15,-17,5,11,grey)
    kotak(-15,-22,5,6,grey)
    kotak(-14,0,5,31,black)
    kotak(17,4,5,5,black)
    kotak(22,23,19,5,black)
    kotak(27,40,21,5,black)
    kotak(20,50,10,8,black)
    kotak(-20,50,6,48,black)
    kotak(-25,44,4,5,black)
    kotak(-30,40,30,5,black)
    kotak(-25,10,6,5,black)
    kotak(-20,4,4,6,black)
    kotak(-25,0,7,5,black)
    kotak(-30,-7,14,5,black)
    kotak(-25,-17,4,5,black)
    kotak(-20,-13,18,5,black)
    kotak(-15,-27,4,5,black)
    kotak(-10,-22,5,7,black)
    kotak(-3,-22,9,6,black)
    kotak(2,-22,9,4,black)
    kotak(6,-27,4,6,black)
    kotak(12,-5,7,5,black)
    kotak(12,-11,6,4,black)
    kotak(12,-17,10,5,black)
    kotak(17,-7,5,5,black)
    kotak(17,-17,5,9,black)
    kotak(21,-11,6,5,black)
    kotak(14,19,9,6,black)  # Eye
    kotak(-10,19,9,6,black) # Eye

def mySpecialKeyboard(key, x, y): 
    global xPosition
    global yPosition
    if key == GLUT_KEY_LEFT:
        xPosition -= 50
        if xPosition <= -80:
            xPosition +=50
    elif key == GLUT_KEY_RIGHT:
        xPosition += 50
        if xPosition >= 1850:
            xPosition -=50
    elif key == GLUT_KEY_UP:
        yPosition += 50
        if yPosition >= 400:
            yPosition -=50
    elif key == GLUT_KEY_DOWN:
        yPosition -= 50
        if yPosition <= -350:
            yPosition +=50
    print(xPosition , ' ', yPosition)

def kotak2(x,y,height,width,color):
    glBegin(GL_POLYGON) 
    glColor3ub(color[0],color[1],color[2])
    glVertex2f(x , y) # pojok kiri atas
    glVertex2f(x , y - height)
    glVertex2f(x + width , y - height)
    glVertex2f(x + width , y)
    glEnd()

def char2():
    kotak2(-200,-200,50,50,black)


#=== Engine =====================================================================

def mouse_play_game(button, state, x, y):       # Click start game
    global play
    if button == GLUT_LEFT_BUTTON:
        if 526 <= x <= 900 and 225 <=y<=298:
            play = True
        print(x,' ',y)

def start_game():
    glPushMatrix()
    glColor3b(36, 150, 127)
    glBegin(GL_QUADS)
    glVertex2f(-300,-500) 
    glVertex2f(-300,-600) 
    glVertex2f(200,-600) 
    glVertex2f(200,-500) 
    glEnd()
    glColor3ub(0,0,0)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-300,-500) 
    glVertex2f(-300,-600) 
    glVertex2f(200,-600) 
    glVertex2f(200,-500) 
    glEnd()
    glPopMatrix()
    drawTextBold("P L A Y G A M E",-140,-560)

def play_game():
    scorebord()
    char2()
    char1() 

#================================================================================


def iterate():
    glViewport(0, 0, 1500, 1500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000, 1000, -1000, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    if play == False:
        start_game()
    else:
        play_game()
    # play_game()
    glutSwapBuffers() #utk membersihkan layar, double buffering

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1450, 600)
    glutInitWindowPosition(30, 100)
    wind = glutCreateWindow("My Game")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(mySpecialKeyboard)
    glutMouseFunc(mouse_play_game)
    glutMainLoop()

main()