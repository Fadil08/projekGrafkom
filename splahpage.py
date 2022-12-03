from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

w,h= 1200,600
xposition=255
yposition=170
post_x = 255
post_y = 170
node_x=[]
node_y=[]
angka1 = random.randrange(1,10)
angka2 = random.randrange(1,10)
salah = angka2+angka2
benar = angka1+angka2
jawaban = [benar,salah]
rand_idx = random.randint(0,1)
jawaban_kiri = jawaban[rand_idx]
jawaban.pop(rand_idx)
jawaban_kanan = jawaban[0]
Soal_rintangan = False
point = 0



class assets:
    def __init__(self,_color):
        self.color = _color if type(_color)==set or _color!='' else (255,255,255)

    def quads(self,_x_min,_x_max,_y_min,_y_max):
        glPushMatrix()
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glBegin(GL_POLYGON)
        glVertex2f(_x_min,_y_min)
        glVertex2f(_x_max,_y_min)
        # glColor3ub(_color[0],_color[1],_color[2])
        glVertex2f(_x_max,_y_max)
        glVertex2f(_x_min,_y_max)
        glEnd()
        glPopMatrix()
    def quads_kiribawah(self,_x_min,_x_max,_y_min,_y_max,_color):
        glPushMatrix()
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glBegin(GL_POLYGON)
        glVertex2f(_x_min,_y_min)
        glColor3ub(_color[0],_color[1],_color[2])
        glVertex2f(_x_max,_y_min)
        glVertex2f(_x_max,_y_max)
        glVertex2f(_x_min,_y_max)
        glEnd()
        glPopMatrix()
    def quads_tengah(self,_x_min,_x_max,_y_min,_y_max,_color):
        glPushMatrix()
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glBegin(GL_POLYGON)
        glVertex2f(_x_min,_y_min)
        glVertex2f(_x_max,_y_min)
        glColor3ub(_color[0],_color[1],_color[2])
        glVertex2f(_x_max,_y_max)
        glVertex2f(_x_min,_y_max)
        glEnd()
        glPopMatrix()
    def quads_kiri_atas(self,_x_min,_x_max,_y_min,_y_max,_color):
        glPushMatrix()
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glBegin(GL_POLYGON)
        glVertex2f(_x_min,_y_min)
        glVertex2f(_x_max,_y_min)
        glVertex2f(_x_max,_y_max)
        glColor3ub(_color[0],_color[1],_color[2])
        glVertex2f(_x_min,_y_max)
        glEnd()
        glPopMatrix()

    def circle(self,r,xR,yR):
        glPushMatrix()
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glBegin(GL_POLYGON)
        for i in range(360):
            theta= 2 *3.1415926*i/360
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + xR, y + yR)
        glEnd();
        glPopMatrix()

    def create_line(self,x1,y1,x2,y2,z):
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glLineWidth(z)
        glBegin(GL_LINE_STRIP)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
        glEnd();
        
    def drawBitmapText(self,string,x,y,z) :
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glRasterPos3f(x,y,z)
        for c in string :
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(c))
    def drawBitmapTextInt(self,int,x,y,z) :
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glRasterPos3f(x,y,z)
        for c in int :
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(c))
    def drawBitmapTextstart(self,string,x,y,z) :
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glRasterPos3f(x,y,z)
        for c in string :
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(c))


class splashPage:
    def bacgrond():
        # bacgrond
        assets((105,200,255)).quads(0,1200,0,600)
        #tanah
        assets((207, 63, 10)).quads(0,1200,0,50)
        # rumput
        assets((0,255,0)).quads(0,1200,50,75)
        # awan1
        assets((255,255,255)).circle(25,150,400)
        assets((255,255,255)).circle(25,175,400)
        assets((255,255,255)).circle(25,200,400)
        # awan2
        assets((255,255,255)).circle(25,500,450)
        assets((255,255,255)).circle(25,525,450)
        assets((255,255,255)).circle(25,550,450)
        # awan 3
        assets((255,255,255)).circle(25,850,450)
        assets((255,255,255)).circle(25,875,450)
        assets((255,255,255)).circle(25,900,450)
        # membuat rumah
        assets((47,79,79)).quads(350,700,80,100)
        # cerobong asap
        assets((47,79,79)).quads(440,460,280,330)
        #bagan rumah
        glBegin(GL_POLYGON)
        glColor(0,0,1)
        glVertex2f(525, 350)
        glVertex2f(400, 250)
        glVertex2f(400,100)
        glVertex2f(650,100)
        glVertex2f(650,250)
        glEnd();
        #atap kiri
        glBegin(GL_QUADS)
        glColor3ub(207, 63, 10)
        glVertex2f(390,250)
        glVertex2f(400,250)
        glVertex2f(525,350)
        glVertex2f(525, 360)
        glEnd();
        #atap kanan
        glBegin(GL_QUADS)
        glColor3ub(207, 63, 10)
        glVertex2f(660,250)
        glVertex2f(650,250)
        glVertex2f(525,350)
        glVertex2f(525, 360)
        glEnd();
        # atap cerobong
        assets((1, 1, 1)).quads(430,470,325,330)
        #tangga 1
        assets((255,255,255)).quads(540,620,100,110)
        #tangga 2
        assets((1,1,1)).quads(550,610,110,120)
        # Pintu
        assets((238,118,0)).quads(555,605,120,210)
        # pegangan pintu
        assets((1,1,1)).circle(5,560,165)
        # membuat jendela
        assets((205,102,29)).quads(430,480,180,230)
        # line atap rumah
        assets((1,1,1)).create_line(400,250,390,250,2)
        assets((1,1,1)).create_line(390,250,525,360,2)
        assets((1,1,1)).create_line(525,360,660,250,2)
        assets((1,1,1)).create_line(660,250,650,250,2)
        # line jendela
        assets((255,255,255)).create_line(480,180,480,230,2)
        assets((255,255,255)).create_line(480,230,430,230,2)
        assets((255,255,255)).create_line(430,230,430,180,2)
        assets((255,255,255)).create_line(430,180,480,180,2)
        assets((255,255,255)).create_line(455,230,455,210,2)
        assets((255,255,255)).create_line(455,210,480,210,2)
        assets((255,255,255)).create_line(455,210,455,180,2)
        # tombol button
    def buttonSTR():
        glPushMatrix()
        assets((0,255,0)).quads(490,560,230,260)
        assets((0,255,0)).circle(16,500,245)
        assets((0,255,0)).circle(16,553,245)
        glPopMatrix()
    def drawtext():
        assets((255,255,255)).drawBitmapText("Welcome Labmat Player",400,375,0)
        assets((255,255,255)).drawBitmapTextstart("Start",497,240,0)
    def btnklik(button,state,x,y):
        global play,point
        if button == GLUT_LEFT_BUTTON:
            if 489<=x<=560 and 340<=y<=370:
                play=True  
           
        elif button == GLUT_LEFT_BUTTON:
            if 930< x < 955 and 350<y<375 == jawaban_kiri:
                point+=100
        elif button == GLUT_LEFT_BUTTON:
            if 1020< x< 1050 and 350<y<375 ==jawaban_kanan:
                point+=100 
        print(x,' ',y)
        print(point)
    def run_splah():
        glPushMatrix()
        splashPage.bacgrond()
        splashPage.buttonSTR()
        splashPage.drawtext()
        
        glPopMatrix()


class labmath:
    def __init__(self,_x_min,_x_max,_y_min,_y_max):
        # self.color = _color if type(_color)==set or _color!='' else (255,255,255)
        self._x_min = _x_min
        self._x_max = _x_max
        self._y_min = _y_min
        self._y_max = _y_max
        self.actual_x_user = 255
        self.actual_y_user = 180
        self.xTranslate = 0
        self.yTranslate = 0
    def quads(self):
        glBegin(GL_QUADS)
        glColor3ub(105,105,105)
        glVertex2f(self._x_min,self._y_min)
        glVertex2f(self._x_max,self._y_min)
        glVertex2f(self._x_max,self._y_max)
        glVertex2f(self._x_min,self._y_max)
        glEnd()
    def create_line(self):
        # glTranslated(self.xTranslate,self.yTranslate,0)
        global node_x,node_y
        glColor3ub(1,1,1)
        glLineWidth(10)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self._x_min,self._y_min)
        glVertex2f(self._x_max,self._y_max)
        # print(self._y_min,self._x_max)
        glEnd();
        
        # save every possible wall location
        if self._x_min > self._x_max:
            new_x = [*range(self._x_max, self._x_min, 5)] # 5 for step movement
        elif self._x_min == self._x_max:
            new_x = [self._x_max] # or x min, bebas
        else:
            new_x = [*range(self._x_min, self._x_max, 5)] # 5 for step movement
            
        if self._y_min > self._y_max:
            new_y = [*range(self._y_max, self._y_min, 5)] # 5 for step movement
        elif self._y_min == self._y_max:
            new_y = [self._y_max] # or x min, bebas
        else:
            new_y = [*range(self._y_min, self._y_max, 5)] # 5 for step movement
        
        if new_x not in node_x and new_y not in node_y:
            node_x.append(new_x)
            node_y.append(new_y)
            

    def circle(self,r,xR,yR):
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glBegin(GL_POLYGON)
        for i in range(360):
            theta= 2 *3.1415926*i/360
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + xR, y + yR)
        glEnd();

    def rintangan(rtg_x_pos,rtg_y_pos,z):

        glPushMatrix()
        glTranslated (rtg_x_pos,rtg_y_pos,z)
        assets((255,255,255)).circle(7,10,10)
        assets((1,1,1)).circle(2,7,10)
        assets((1,1,1)).circle(2,12,10)
        glPopMatrix()

    def page_soal(x_pos_page,y_pos_page,z):
        global angka1,angka2,jawaban_kiri,jawaban_kanan
        glPushMatrix()
        glTranslated(x_pos_page,y_pos_page,z)
        assets((0,250,154)).quads_kiri_atas(0,200,0,200,(1,2,3))
        assets((255,255,255)).quads_kiribawah(30,160,140,180,(0, 255 ,255))
        assets((255,255,255)).quads_kiri_atas(30,160,90,120,(0, 255 ,255))
        assets((255,255,255)).quads_kiribawah(30,50,25,50,(0, 255 ,255))
        assets((255,255,255)).quads_kiribawah(120,140,25,50,(0, 255 ,255))
        assets((1,1,1)).drawBitmapText("page Soal",40,150,0)
        assets((1,1,1)).drawBitmapText(f'{angka1} + {angka2} =',50,100,0)
        assets((1,1,1)).drawBitmapText(f'{jawaban_kiri}',30,30,0)
        assets((1,1,1)).drawBitmapText(f'{jawaban_kanan}',120,30,0)
        glPopMatrix()

    def point(x_pos_soal,y_pos_soal,z):
        glPushMatrix()
        glTranslated (x_pos_soal,y_pos_soal,z)
        assets((255,255,255)).circle(7,10,10)
        glPopMatrix()
    def labirin():
        # (xmin,xmax,ymin,ymax)xmin ymin = titik awal, xmax,ymax titik tujuan
        # line melingkar 
        assets((238,154,0)).quads(0,1200,0,600)
        # assets()
        # labmath(0,1200,0,600).quads()
        labmath(450,300,200,200).create_line()
        labmath(300,300,200,300).create_line()
        labmath(300,200,300,300).create_line()
        labmath(200,200,300,550).create_line()
        labmath(200,700,550,550).create_line()
        labmath(700,700,550,450).create_line()
        # # line melingkar ke kanan
        labmath(750,700,350,350).create_line()
        labmath(700,700,350,400).create_line()
        labmath(700,750,400,400).create_line()
        labmath(750,750,400,500).create_line()
        labmath(750,800,500,500).create_line()
        labmath(800,800,500,50).create_line()
        labmath(800,300,50,50).create_line()
        labmath(300,300,50,150).create_line()
        labmath(300,400,150,150).create_line()
        # cabang1
        labmath(200,300,400,400).create_line()
        labmath(300,300,400,350).create_line()
        # cabang2 dari kiri
        labmath(200,250,350,350).create_line()
        labmath(250,250,550,450).create_line()

        labmath(450,450,550,500).create_line()
        labmath(450,350,500,500).create_line()

        labmath(550,500,500,500).create_line()

        labmath(600,600,550,500).create_line()
        labmath(600,650,500,500).create_line()
        labmath(650,650,500,300).create_line()
        labmath(650,600,300,300).create_line()
        labmath(600,650,300,300).create_line()
        labmath(650,650,300,250).create_line()
        labmath(650,600,250,250).create_line()
        labmath(600,650,250,250).create_line()
        labmath(650,700,200,200).create_line()
        labmath(700,700,200,250).create_line()

        # titik mulai j1
        labmath(800,750,200,200).create_line()
        labmath(750,750,200,300).create_line()
        labmath(750,700,300,300).create_line()
        # titik mulai i1
        labmath(800,600,150,150).create_line()
        labmath(600,600,150,100).create_line()
        labmath(600,500,100,100).create_line()

        labmath(600,550,150,150).create_line()
        labmath(550,550,150,200).create_line()
        labmath(550,500,200,200).create_line()
        labmath(500,500,200,150).create_line()
        labmath(500,500,150,350).create_line()
        labmath(500,450,350,350).create_line()
        labmath(500,600,350,350).create_line()
        labmath(600,600,350,450).create_line()
        # mlai titik p2
        labmath(500,500,350,400).create_line()
        labmath(500,350,400,400).create_line()
        labmath(350,350,400,400).create_line()
        labmath(350,350,400,450).create_line()
        labmath(350,450,450,450).create_line()
        # mulai titik n2
        labmath(550,550,400,450).create_line()
        labmath(550,500,450,450).create_line()
        # mulai tiitk n
        labmath(450,450,150,100).create_line()
        labmath(450,400,100,100).create_line()
        # mulai titik f3 
        labmath(350,350,250,350).create_line()
        labmath(350,400,350,350).create_line()
    def user():
        glTranslated(xposition,yposition,0)
        glBegin(GL_QUADS)
        glColor3ub(105,105,105)
        glVertex2f(0,0)
        glVertex2f(25,0)
        glVertex2f(25,20)
        glVertex2f(0,20)
        glEnd()
        # kaki kiri
        glBegin(GL_QUADS)
        glColor3ub(105,105,105)
        glVertex2f(5,0)
        glVertex2f(10,0)
        glVertex2f(10,-10)
        glVertex2f(5,-10)
        glEnd()
        # kaki kanan 
        glBegin(GL_QUADS)
        glColor3ub(105,105,105)
        glVertex2f(15,0)
        glVertex2f(20,0)
        glVertex2f(20,-10)
        glVertex2f(15,-10)
        glEnd()
        # glColor3ub(105,105,105)
        # glVertex2f(260,160)
        # glVertex2f(265,160)
        # glVertex2f(265,170)
        # glVertex2f(260,170)
        # glEnd()
        # mata kiri
        glBegin(GL_POLYGON)
        glColor3ub(255,255,255)
        for i in range(360):
            theta= 2 *3.1415926*i/360
            x = 4 * math.cos(theta) 
            y = 4 * math.sin(theta)
            glVertex2f(x + 7.5, y + 10 )
        glEnd()
        glBegin(GL_POLYGON)
        glColor3ub(0,0,0)
        for i in range(360):
            theta= 2 *3.1415926*i/360
            x = 2 * math.cos(theta)
            y = 2 * math.sin(theta)
            glVertex2f(x + 7.5, y + 10 )
        glEnd()
        # mata kanan
        glBegin(GL_POLYGON)
        glColor3ub(255,255,255)
        for i in range(360):
            theta= 2 *3.1415926*i/360
            x = 4 * math.cos(theta)
            y = 4 * math.sin(theta)
            glVertex2f(x + 17.25, y + 10 )
        glEnd()
        glBegin(GL_POLYGON)
        glColor3ub(0,0,0)
        for i in range(360):
            theta= 2 *3.1415926*i/360
            x = 2 * math.cos(theta)
            y = 2 * math.sin(theta)
            glVertex2f(x + 17.25, y + 10 )
        glEnd()
    def run_labirin():
        labmath.labirin()
        # labmath.page_soal(900,200,0)
        # labmath.rintangan(215,370,0)
        labmath.user()
    # def colision():
    #     global xposition,yposition
    #     for i in range(len(node_x)):
    #         print (node_x[i])
    #         if node_x[i][0] > node_x[i][1]:
    #             if node_x[i][1] < xposition < node_x[i][0]:
    #                 # xposition+=5
    #                 print('kolision')
                
    #         else:
    #             if node_x[i][0] < xposition<node_x[i][1]:
    #                 print('salah')
                
    def mySpecialKeyboard(key,x,y):
        global xposition,yposition,point
        
        col_left = False
        col_right = False
        col_bot = False
        col_top = False
        
        for (wall_x, wall_y) in zip(node_x, node_y):
            if xposition-10 in wall_x and yposition in wall_y:
                col_left = True
                break
            elif xposition+25 in wall_x and yposition in wall_y:
                col_right = True
                break
            elif yposition+10 in wall_y and xposition in wall_x:
                col_top = True
                break
            elif yposition-15 in wall_y and xposition in wall_x:
                col_bot = True
                break
            elif 60 <=yposition <=130 and xposition <310:
                col_left = True
                break
            elif 390 <=xposition <=420 and yposition <115:
                col_bot = True
                col_top = True
                break
            elif 530 <=xposition <=775 and yposition> 125:
                col_top = True
                break
            elif 500 <=xposition <=525 and 175>yposition> 185:
                col_top = True
                col_bot = True
                break
            
            # colision rintangan
            if 210 <= xposition<220 :
                pass
        print("LeftCollision", col_left, "| TopCollision", col_top, "| RightCollision", col_right, "| BottomCollision", col_bot)
            
        if key == GLUT_KEY_LEFT and not col_left:
            xposition -= 5
        elif key == GLUT_KEY_RIGHT and not col_right:
            xposition += 5
        elif key == GLUT_KEY_UP and not col_top:
            yposition += 5
        elif key == GLUT_KEY_DOWN and not col_bot: 
            yposition -= 5
        # elif xposition == 
        
        print(xposition,' ',yposition)
        print(point)
    def mykeyboard(key,x,y):
        global point
        if key == b'1':
            if jawaban_kiri == benar:
                poin+=10
        elif key == b'2':
            if jawaban_kanan == benar:
                point +=100
        print(point)
        
class Game:
    def __init__(self) -> None:
        self.angka1 = random.randrange(1,10)
        self.angka2 = random.randrange(1,10)
        self.salah = self.angka2+self.angka2
        self.benar = self.angka1+self.angka2
        self.jawaban = [self.benar,self.salah]
        self.rand_idx = random.randint(0,1)
        self.jawaban_kiri = self.jawaban[rand_idx]
        self.jawaban.pop(self.rand_idx)
        self.jawaban_kanan = self.jawaban[0]
        self.Soal_rintangan1 = False
        self.x_pos_rtg1 =0 
        self.y_pos_rtg1 =0
        self.point = 0
    def rintangan():
        glPushMatrix()
        glTranslated (rtg_x_pos,rtg_y_pos)
        assets((255,255,255)).circle(7,10,10)
        assets((1,1,1)).circle(2,7,10)
        assets((1,1,1)).circle(2,12,10)
        glPopMatrix()
    def point(x_pos_soal,y_pos_soal,z):
        glPushMatrix()
        glTranslated (x_pos_soal,y_pos_soal,z)
        assets((255,255,255)).circle(7,10,10)
        glPopMatrix()
    def page_soal(self,x_pos_page,y_pos_page):
        glPushMatrix()
        glTranslated(x_pos_page,y_pos_page,0)
        assets((0,250,154)).quads_kiri_atas(0,200,0,200,(1,2,3))
        assets((255,255,255)).quads_kiribawah(30,160,140,180,(0, 255 ,255))
        assets((255,255,255)).quads_kiri_atas(30,160,90,120,(0, 255 ,255))
        assets((255,255,255)).quads_kiribawah(30,50,25,50,(0, 255 ,255))
        assets((255,255,255)).quads_kiribawah(120,140,25,50,(0, 255 ,255))
        assets((1,1,1)).drawBitmapText("page Soal",40,150,0)
        assets((1,1,1)).drawBitmapText(f'{self.angka1} + {self.angka2} =',50,100,0)
        assets((1,1,1)).drawBitmapText(f'{self.jawaban_kiri}',30,30,0)
        assets((1,1,1)).drawBitmapText(f'{self.jawaban_kanan}',120,30,0)
        glPopMatrix()
    def mulai():
        labmath.labirin()
        game = Game()
        game.page_soal(900,200) 
        labmath.user()   
        



def iterate():
    glViewport(0, 0, 1200, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1200, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    # splashPage.run_splah()
    # labmath.labirin()
    Game.mulai()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("LabMath")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(labmath.mySpecialKeyboard)
    glutKeyboardFunc(labmath.mykeyboard)
    glutMouseFunc(splashPage.btnklik)

    glutMainLoop()

main()