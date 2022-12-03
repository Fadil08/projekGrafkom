from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *




# Koordinat x dan y untuk posisi kotak
pos_x_tombol = 0
pos_y_tombol = 400

pos_x_kotak = 0
pos_y_kotak = -200

pos_x_apel = 0
pos_y_apel = 400

max_gravity = 7
aksel    = 2

hijau = 1
biru = 1
merah = 1


gameMulai = False

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

# Membuat bentuk kotak

def tombolPlay():
    global pos_x_tombol, pos_y_tombol
    glPushMatrix()
    glColor3ub(102, 255, 0)
    glTranslated(pos_x_tombol,pos_y_tombol,0)

    glBegin(GL_QUADS)
    glVertex2f(-20,-20)
    glVertex2f(20,-20)
    glVertex2f(20,20)
    glVertex2f(-20,20)

    glEnd()
    glPopMatrix()
    

def apel():
    global pos_x_apel, pos_y_apel, pos_x_kotak, pos_y_kotak


    glPushMatrix()
    glColor3f(merah,0,0)
    glTranslated(pos_x_apel,pos_y_apel,0)

    #collision player dan apel
    if pos_x_apel == pos_x_kotak and pos_y_apel == pos_y_kotak:
        print("aduh kena apel")

    #gimana apel bisa jatuh
    pos_y_apel -= 5

    #kalo dah sampe bawah bikin dari atas lagi
    # print("y apel:",pos_y_apel)
    if pos_y_apel < -500:
        pos_y_apel = 400
        # print(pos_y_apel)

    glBegin(GL_TRIANGLES)
    # Kiri Atas
    glVertex2f(-50,-50)
    # Kanan Atas
    glVertex2f(50,-50)
    # Kanan Bawah
    glVertex2f(50,50)
    # Kiri Bawa
    glEnd()
    glPopMatrix()
# class assets:
#     def __init__(self):
#         self.Translate_x = 0
#         self.Translate_y = 0
#         self.nodex = []
#         self.nodey = []

#     def quads(self,_x_min,_x_max,_y_min,_y_max):
#         glTranslated(_x_max,_y_min,0)
#         glPushMatrix()
#         glBegin(GL_POLYGON)
#         glColor3ub(255,0,0)
#         glVertex2f(_x_min,_y_min)
#         glVertex2f(_x_max,_y_min)
#         glVertex2f(_x_max,_y_max)
#         glVertex2f(_x_min,_y_max)
#         glEnd()
#         glPopMatrix()
#         self.nodey.append([_y_min,_y_max])
#         self.nodex.append([_x_min,_x_max])    
#     def aset():
#         assets().quads(50,100,100,100)
    
def kotak():
    global pos_x_kotak, pos_y_kotak
    global max_gravity
    glPushMatrix()
    # pos_y_kotak -= 2 

    if pos_x_kotak >= 440:
        pos_x_kotak = 440
    print(pos_y_kotak)

    if pos_y_kotak < max_gravity:
        pos_y_kotak = pos_y_kotak

    # print("posisi_x: ", pos_x_kotak)

    glColor3f(hijau,biru,merah)
    glTranslated(pos_x_kotak, pos_y_kotak, 0)

    glBegin(GL_POLYGON)
    # Kiri Atas
    glVertex2f(-50,-50)
    # Kanan Atas
    glVertex2f(50,-50)
    # Kanan Bawah
    glVertex2f(50,50)
    # Kiri Bawah
    glVertex2f(-50,50)
    glEnd()
    glPopMatrix()
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(255,255,255)
    
    if gameMulai == True:
        kotak()
        apel()
        # assets.aset()
    else:
        tombolPlay()
        # assets.aset()
        
    glFlush()
    

def input_untuk_mouse(button, state, x,y):
    global pos_x_tombol, gameMulai
    if button == GLUT_LEFT_BUTTON and x >= 240 and x <= 260 and y >= 40 and y <=60:
        print("start")
        # pos_x_tombol -= 40

    # if button == GLUT_RIGHT_BUTTON and pos_x_tombol == 0 and pos_y_tombol == 400:
    # print(x,y)
        gameMulai = True


def input_keyboard(key,x,y):
    global pos_x_kotak, pos_y_kotak
    if key == GLUT_KEY_UP:
        pos_y_kotak = 10
    elif key == GLUT_KEY_DOWN:
        pos_y_kotak -= 5
    elif key == GLUT_KEY_RIGHT:
        pos_x_kotak += 5
    elif key == GLUT_KEY_LEFT:
        pos_x_kotak -= 5
        

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("collision")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    glutMouseFunc(input_untuk_mouse)
    glutTimerFunc(1,update,0)
    init()
    glutMainLoop()

main()