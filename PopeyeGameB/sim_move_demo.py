import sys
import  random
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow

from key_notifier import KeyNotifier
from oliveMovement import OliveMovement
from badzoMovement import BadzoMovement


class SimMoveDemo(QMainWindow):

    def __init__(self):
        super().__init__()

        oImage = QImage("images\\backround.png")
        sImage = oImage.scaled(QSize(1920, 1080))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)


        self.pix1 = QPixmap('images\\Popeye.png')
        self.pix2 = QPixmap('images\\oliveOyl.png')

        self.pix4 = QPixmap('images\\Ladders.png')
        self.pix5 = QPixmap('images\\Ladders.png')
        self.pix6 = QPixmap('images\\Ladders.png')
        self.pix7 = QPixmap('images\\Ladders.png')
        self.pix3 = QPixmap('images\\Badzo.png')
        self.pix30 = QPixmap('images\\BadzoR.png')

        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)
        self.label6 = QLabel(self)
        self.label7 = QLabel(self)
        self.label3 = QLabel(self)
        self.label30 = QLabel(self)

        self.hitFloor = False
        self.hitSide = False

        self.hitSide2 = False
        self.LadderUPBadzo = False
        self.PopeoSe = False
        self.KolkoSePopeo = 0

        self.LadderDownBadzo = False
        self.SisaoDole=False
        self.KolkoJeSisao=0
        self.hitFloor2 = False
        self.boolSkok=False

        self.sprat=1
        #self.timerP1 = QTimer(self)
        #self.timerP1.setInterval(2000)
        #self.timerP1.setSingleShot(True)

        #self.timerP2 = QTimer(self)
        #self.timerP2.setInterval(2000)
        #self.timerP2.setSingleShot(True)

        self.setWindowState(Qt.WindowFullScreen)
        self.__init_ui__()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        self.oliveMovement = OliveMovement()
        self.oliveMovement.oliveMovementSignal.connect(self.moveOlive)
        self.oliveMovement.start()

        self.badzoMovement = BadzoMovement()
        self.badzoMovement.badzoMovementSignal.connect(self.moveBadzo)
        self.badzoMovement.start()

    def __init_ui__(self):

        font = QtGui.QFont()
        font.setPointSize(40)

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(1000, 953, 75, 75)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(550, 250, 75, 100)



        self.label4.setPixmap(self.pix4)
        self.randx=random.randint(300, 1500)
        p=self.randx%10
        self.merdevine1=self.randx-p
        self.BoolBadzaMerdevine = False
        self.label4.setGeometry(self.merdevine1,650, 90, 180)


        self.label5.setPixmap(self.pix5)
        self.randx2=random.randint(300, 1500)
        p1=self.randx2%10
        self.merdevine2=self.randx2-p1
       # self.BoolBadzaMerdevine = False
        self.label5.setGeometry(self.merdevine2,850, 90, 180)

        self.label6.setPixmap(self.pix6)
        self.label6.setGeometry(300, 460, 90, 180)

        self.label7.setPixmap(self.pix6)
        self.label7.setGeometry(1500, 460, 90, 180)

        self.label3.setPixmap(self.pix3)
        self.label3.setGeometry(300, 570, 85, 75)

       # self.label30.setPixmap(self.pix30)
        #self.label30.setGeometry(300, 570, 85, 75)

        self.setWindowTitle('Popeye')
        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        rec1 = self.label1.geometry()

        if key == Qt.Key_Right:
            if (rec1.x() < 1800 and (rec1.y() < 960 and rec1.y() > 935) or (rec1.y() > 755 and rec1.y() < 780) or (
                    rec1.y() > 550 and rec1.y() < 575) or ((rec1.y() > 371 and rec1.y() < 381) and (rec1.x() < 450 or rec1.x() >= 1400))):
                self.label1.setGeometry(rec1.x() + 10, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            if (rec1.x() > 50 and rec1.x() < 305 and rec1.y() < 952):
                if ((rec1.x() >= 300 and rec1.x() <= 302) and (rec1.y() <= 952 and rec1.y() >= 915)):
                    self.label1.setGeometry(rec1.x() + 10, rec1.y() + 10, rec1.width(), rec1.height())
                if ((rec1.x() >= 270 and rec1.x() <= 300) and (rec1.y() <= 950 and rec1.y() >= 915)):
                    self.label1.setGeometry(rec1.x() + 10, rec1.y() + 10, rec1.width(), rec1.height())
                elif ((rec1.x() >= 238 and rec1.x() < 270) and (rec1.y() < 915 and rec1.y() >= 878)):
                    self.label1.setGeometry(rec1.x() + 10, rec1.y() + 10, rec1.width(), rec1.height())
                elif (rec1.x() >= 203 and rec1.x() < 240 and (rec1.y() < 883 and rec1.y() >= 841)):
                    self.label1.setGeometry(rec1.x() + 10, rec1.y() + 10, rec1.width(), rec1.height())
                elif (rec1.x() >= 170 and rec1.x() < 203 and (rec1.y() < 853 and rec1.y() >= 805)):
                    self.label1.setGeometry(rec1.x() + 10, rec1.y() + 10, rec1.width(), rec1.height())
                elif ((rec1.x() >= 120 and rec1.x() < 170) and (rec1.y() < 845 and rec1.y() >= 750)):
                    self.label1.setGeometry(rec1.x() + 10, rec1.y() + 10, rec1.width(), rec1.height())
            if (rec1.y() < 947 and rec1.y() <= 760 and(rec1.x() > self.merdevine1 and rec1.x() < self.merdevine1 + 50) and rec1.y() >= 380):
                self.label1.setGeometry(rec1.x(), rec1.y() + 10, rec1.width(), rec1.height())
            if (rec1.y() >750 and (rec1.x() > self.merdevine2 and rec1.x() < self.merdevine2 + 50) and rec1.y() <= 950):
                self.label1.setGeometry(rec1.x(), rec1.y() + 10, rec1.width(), rec1.height())
            if ((rec1.x() <= 1530 and rec1.x() >= 1500) and (rec1.y() <= 560 and rec1.y() >= 370)):
                self.label1.setGeometry(rec1.x(), rec1.y() + 10, rec1.width(), rec1.height())
            if ((rec1.x() <= 330 and rec1.x() >= 300) and (rec1.y() <= 560 and rec1.y() >= 370)):
                self.label1.setGeometry(rec1.x(), rec1.y() + 10, rec1.width(), rec1.height())

        elif key == Qt.Key_Up:
            if (rec1.x() > 50 and rec1.x() <= 303):
                if ((rec1.x() >= 300 and rec1.x() <= 302) and (rec1.y() <= 952 and rec1.y() >= 915)):
                    self.label1.setGeometry(rec1.x() - 10, rec1.y() - 10, rec1.width(), rec1.height())
                if ((rec1.x() >= 270 and rec1.x() <= 300) and (rec1.y() <= 950 and rec1.y() >= 915)):
                    self.label1.setGeometry(rec1.x() - 10, rec1.y() - 10, rec1.width(), rec1.height())
                elif ((rec1.x() >= 238 and rec1.x() < 270) and (rec1.y() < 915 and rec1.y() >= 878)):
                    self.label1.setGeometry(rec1.x() - 10, rec1.y() - 10, rec1.width(), rec1.height())
                elif (rec1.x() >= 203 and rec1.x() < 240 and (rec1.y() < 883 and rec1.y() >= 841)):
                    self.label1.setGeometry(rec1.x() - 10, rec1.y() - 10, rec1.width(), rec1.height())
                elif (rec1.x() >= 170 and rec1.x() < 203 and (rec1.y() < 853 and rec1.y() >= 805)):
                    self.label1.setGeometry(rec1.x() - 10, rec1.y() - 10, rec1.width(), rec1.height())
                elif ((rec1.x() >= 120 and rec1.x() < 170) and (rec1.y() < 845 and rec1.y() >= 750)):
                    self.label1.setGeometry(rec1.x() - 10, rec1.y() - 10, rec1.width(), rec1.height())
            if (rec1.y() > 50 and (rec1.x() > self.merdevine1 and rec1.x() < self.merdevine1 + 50) and rec1.y() >= 570): #and rec1.y() > 380):
                self.label1.setGeometry(rec1.x(), rec1.y() - 10, rec1.width(), rec1.height())
            if (rec1.y() > 50 and (rec1.x() > self.merdevine2 and rec1.x() < self.merdevine2 + 50) and rec1.y() >= 780):
                self.label1.setGeometry(rec1.x(), rec1.y() - 10, rec1.width(), rec1.height())
            if ((rec1.x() <= 1530 and rec1.x() >= 1500) and (rec1.y() <= 580 and rec1.y() >= 385)):
                self.label1.setGeometry(rec1.x(), rec1.y() - 10, rec1.width(), rec1.height())
            if ((rec1.x() <= 330 and rec1.x() >= 300) and (rec1.y() <= 580 and rec1.y() >= 385)):
                self.label1.setGeometry(rec1.x(), rec1.y() - 10, rec1.width(), rec1.height())

        elif key == Qt.Key_Left:
            if (rec1.x() > 50 and ((rec1.y() < 960 and rec1.y() > 935) or (rec1.y() > 755 and rec1.y() < 780) or (
                    rec1.y() > 550 and rec1.y() < 575) or ((rec1.y() > 371 and rec1.y() < 381) and (rec1.x() <= 450 or rec1.x() >= 1450)))):
                self.label1.setGeometry(rec1.x() - 10, rec1.y(), rec1.width(), rec1.height())

    def moveOlive(self):
        rec2 = self.label2.geometry()
        if (rec2.x() == 1300):
            self.hitSide = True
        elif (rec2.x() == 550):
            self.hitSide = False

        if self.hitSide:
            self.label2.setGeometry(rec2.x() - 10, rec2.y() + 0, rec2.width(), rec2.height())
        else:
            self.label2.setGeometry(rec2.x()+10, rec2.y() + 0, rec2.width(), rec2.height())

    def moveBadzo(self):
        #if(self.hitSide):
         #   rec3 = self.label3.geometry()
        #elif(self.hitSide==False):
          #  rec3 = self.label30.geometry()
        rec3 = self.label3.geometry()

        if(self.sprat==1):

            self.boolSkok+=1
            if(rec3.x() == 1500 ):
                self.hitSide2 = True
                self.LadderUPBadzo = self.BoolBadzaMerdevine
                self.boolSkok += 1
            elif(rec3.x() ==self.merdevine1): #or self.boolSkok==True):
                self.LadderDownBadzo=self.BoolBadzaMerdevine
            elif(rec3.x() == 300):
                self.hitSide2 = False
                self.LadderUPBadzo = False


            if self.LadderDownBadzo:
                self.label3.setGeometry(rec3.x() - 0, rec3.y() + 10, rec3.width(), rec3.height())
                self.KolkoJeSisao += 10
                if (self.KolkoJeSisao == 190):
                    self.KolkoJeSisao = 0
                    self.SisaoDole = True
                    self.LadderDownBadzo = False
                    self.BoolBadzaMerdevine = random.randint(0, 1)
                    self.sprat += 1

            elif self.hitSide2:
                self.label3.setGeometry(rec3.x() - 10, rec3.y() + 0, rec3.width(), rec3.height())
                self.BoolBadzaMerdevine = random.randint(0, 1)
                self.boolSkok = random.randint(0, 1)
            elif self.LadderUPBadzo:
                 self.label3.setGeometry(rec3.x() - 0, rec3.y() - 10, rec3.width(), rec3.height())
                 self.KolkoSePopeo += 10
                 if(self.KolkoSePopeo== 190):
                    self.KolkoSePopeo =0
                    self.SisaoDole=False
                    self.LadderUPBadzo = False
                    self.BoolBadzaMerdevine = random.randint(0, 1)
                    self.sprat -= 1
            elif self.hitSide2==False:
                self.label3.setGeometry(rec3.x() + 10, rec3.y() + 0, rec3.width(), rec3.height())
                self.BoolBadzaMerdevine = random.randint(0, 1)


        elif(self.sprat==2):
            if (rec3.x() == 1500):
                self.hitSide2 = True
            elif(rec3.x() == self.merdevine2): #or self.boolSkok == True):
                self.LadderDownBadzo = self.BoolBadzaMerdevine
            elif(rec3.x() == self.merdevine1):
                 self.LadderUPBadzo = self.BoolBadzaMerdevine
            elif (rec3.x() == 300):
                self.hitSide2 = False
                self.LadderUPBadzo = False


            if self.LadderDownBadzo:
                self.label3.setGeometry(rec3.x() - 0, rec3.y() + 10, rec3.width(), rec3.height())
                self.KolkoJeSisao += 10
                if (self.KolkoJeSisao == 190):
                    self.KolkoJeSisao = 0
                    self.SisaoDole = True
                    self.LadderDownBadzo = False
                    self.BoolBadzaMerdevine = random.randint(0, 1)
                    self.sprat += 1

            elif self.hitSide2:
                self.label3.setGeometry(rec3.x() - 10, rec3.y() + 0, rec3.width(), rec3.height())
                self.BoolBadzaMerdevine = random.randint(0, 1)
                self.boolSkok = random.randint(0, 1)
            elif self.LadderUPBadzo:
                self.label3.setGeometry(rec3.x() - 0, rec3.y() - 10, rec3.width(), rec3.height())
                self.KolkoSePopeo += 10
                if (self.KolkoSePopeo == 190):
                    self.KolkoSePopeo = 0
                    self.SisaoDole = False
                    self.LadderUPBadzo = False
                    self.BoolBadzaMerdevine = random.randint(0, 1)
                    self.sprat -= 1

            elif self.hitSide2 == False:
                self.label3.setGeometry(rec3.x() + 10, rec3.y() + 0, rec3.width(), rec3.height())
                self.BoolBadzaMerdevine = random.randint(0, 1)

        elif (self.sprat == 3):
            if (rec3.x() == 1500):
                self.hitSide2 = True
            #elif (rec3.x() == self.merdevine2):
               # self.LadderDownBadzo = self.BoolBadzaMerdevine
            elif (rec3.x() == self.merdevine2):
                self.LadderUPBadzo = self.BoolBadzaMerdevine
            elif (rec3.x() == 300):
                self.hitSide2 = False
                self.LadderUPBadzo = False

            if self.hitSide2:
                self.label3.setGeometry(rec3.x() - 10, rec3.y() + 0, rec3.width(), rec3.height())
                self.BoolBadzaMerdevine = random.randint(0, 1)


            elif self.LadderUPBadzo:
                self.label3.setGeometry(rec3.x() - 0, rec3.y() - 10, rec3.width(), rec3.height())
                self.KolkoSePopeo += 10
                if (self.KolkoSePopeo == 190):
                    self.KolkoSePopeo = 0
                    self.SisaoDole = False
                    self.LadderUPBadzo = False
                    self.BoolBadzaMerdevine = random.randint(0, 1)
                    self.sprat -= 1

            elif self.hitSide2 == False:
                self.label3.setGeometry(rec3.x() + 10, rec3.y() + 0, rec3.width(), rec3.height())
                self.BoolBadzaMerdevine = random.randint(0, 1)

        elif (self.sprat == 0):
            if (rec3.x() == 400 or rec3.x() == 1920):
                self.hitSide2 = True
            elif (rec3.x() == 300 or rec3.x() == 1500 ):
                self.LadderDownBadzo = self.BoolBadzaMerdevine
          #  elif (rec3.x() == self.merdevine1):
               # self.LadderUPBadzo = self.BoolBadzaMerdevine
            elif (rec3.x() == 0 or rec3.x() == 1300):
                self.hitSide2 = False
              #  self.LadderUPBadzo = self.BoolBadzaMerdevine

            if self.hitSide2:
                self.label3.setGeometry(rec3.x() - 10, rec3.y() + 0, rec3.width(), rec3.height())
                self.BoolBadzaMerdevine = random.randint(0, 1)

            elif self.LadderDownBadzo:
                self.label3.setGeometry(rec3.x() - 0, rec3.y() + 10, rec3.width(), rec3.height())
                self.KolkoJeSisao += 10
                if (self.KolkoJeSisao == 190):
                    self.KolkoJeSisao = 0
                    self.SisaoDole = True
                    self.LadderDownBadzo = False
                    self.BoolBadzaMerdevine = random.randint(0, 1)
                    self.sprat += 1

            elif self.LadderUPBadzo:
                self.label3.setGeometry(rec3.x() - 0, rec3.y() - 10, rec3.width(), rec3.height())
                self.KolkoSePopeo += 10
                if (self.KolkoSePopeo == 190):
                    self.KolkoSePopeo = 0
                    self.SisaoDole = False
                    self.LadderUPBadzo = False
                    self.BoolBadzaMerdevine = random.randint(0, 1)
                    self.sprat -= 1

            elif self.hitSide2 == False:
                self.label3.setGeometry(rec3.x() + 10, rec3.y() + 0, rec3.width(), rec3.height())
                self.BoolBadzaMerdevine = random.randint(0, 1)

    def closeEvent(self, event):
        self.key_notifier.die()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
