import sys
import random
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QProgressBar
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow
from multiprocessing import Queue, Process
from key_notifier import KeyNotifier
from oliveMovement import OliveMovement
from badzoMovement import BadzoMovement
from heartMovement import HeartMovement
from random import randint
from HitForce import force, BombsMovement
from rainingMan import RainingBombs
from BadzoFreeze import BadzoFreezeProcess
from key_notifier2 import KeyNotifier2
from Collision import isHit
br = 2
brLevel = 0

class SimMoveDemo(QMainWindow):
    def __init__(self, brojIgraca):
        super().__init__()

        oImage = QImage("images\\backround.png")
        sImage = oImage.scaled(QSize(1920, 1080))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.pix1 = QPixmap('images\\Popeye.png')
        self.pix11 = QPixmap('images\\Popeye.png')      #-----------------
        self.pix2 = QPixmap('images\\oliveOyl.png')

        self.pix4 = QPixmap('images\\Ladders.png')
        self.pix5 = QPixmap('images\\Ladders.png')
        self.pix6 = QPixmap('images\\Ladders.png')
        self.pix7 = QPixmap('images\\Ladders.png')
        self.pix3 = QPixmap('images\\Badzo.png')
        self.pixHeart = QPixmap('images\\plavoSrce.png')
        self.pixBomb = QPixmap('images\\bomb.png')
        self.pix30 = QPixmap('images\\BadzoR.png')
        self.pixForce = QPixmap('images\\force.png')
        self.hearts = []

        self.q = Queue()
        self.bombs = []
        self.unexpectedForce = Process(target=force, args=[self.q])
        self.unexpectedForce.start()
        self.badzoStop = Queue()
        self.badzoStart = Queue()
        self.badzoBug = Process(target=BadzoFreezeProcess, args=[self.badzoStart, self.badzoStop])
        self.badzoBug.start()

        self.hitF = False
        self.zaustavio = False

        self.label1 = QLabel(self)
        self.label11 = QLabel(self)
        self.label2 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)
        self.label6 = QLabel(self)
        self.label7 = QLabel(self)
        self.label3 = QLabel(self)
        self.label30 = QLabel(self)
        self.labelScore = QLabel(self)
        self.labelLifes = QLabel(self)
        self.labelLevel = QLabel(self)
        self.pBar = QProgressBar(self)

        self.labelforce=QLabel(self)
        self.timerP1 = QTimer(self)
        self.timerP2 = QTimer(self)
        self.hitFloor = False
        self.hitSide = False

        self.hitSide2 = False
        self.LadderUPBadzo = False
        self.PopeoSe = False
        self.KolkoSePopeo = 0

        self.LadderDownBadzo = False
        self.SisaoDole = False
        self.KolkoJeSisao = 0
        self.hitFloor2 = False
        self.boolSkok = False

        self.hitLeftUpStairs = False
        self.hitLeftDownStairs = False
        self.hitRightUpStairs = False
        self.hitRightDownStairs = False

        self.hitLeftUpStairsTop = False
        self.hitLeftDownStairsTop = False
        self.hitRightUpStairsTop = False
        self.hitRightDownStairsTop = False

        self.popeyeStep = 10
        self.poeni1 = 0
        self.sprat = 1
        self.setWindowState(Qt.WindowFullScreen)
        self.__init_ui__(br,brLevel)

        self.key_notifier = KeyNotifier()

        if (brojIgraca == 1):
            self.key_notifier.key_signal.connect(self.__update_position__)  # -----------------
            self.brojIgracaJedan = True
        else:
            self.brojIgracaJedan = False
            self.label11.setPixmap(self.pix11)  # ---------------------------
            self.label11.setGeometry(1200, 954, 75, 75)  # -----------------------
            self.key_notifier2 = KeyNotifier2()
            self.key_notifier.key_signal.connect(self.__update_position__)  # -----------------
            self.key_notifier2.key_signal2.connect(self.__update_position2__)  # -----------------
            self.key_notifier2.start()

        self.key_notifier.start()

        self.oliveMovement = OliveMovement()
        self.oliveMovement.oliveMovementSignal.connect(self.moveOlive)
        self.oliveMovement.start()

        self.badzoMovement = BadzoMovement()
        self.badzoMovement.badzoMovementSignal.connect(self.moveBadzo)
        self.badzoMovement.start()

        self.heartMovement = HeartMovement()
        self.heartMovement.heartMovementSignal.connect(self.generateHeart)
        self.heartMovement.start()

        self.bombsMovement = BombsMovement()
        self.bombsMovement.bombsMovementSignal.connect(self.generateBombs)
        self.bombsMovement.start()

        self.rainingBombs = RainingBombs()
        self.rainingBombs.rainingBombsSignal.connect(self.moveBombs)
        self.rainingBombs.start()

    def __init_ui__(self,br,brLevel):

        font = QtGui.QFont()
        font.setPointSize(40)

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(1570, 954, 75, 75)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(550, 250, 75, 100)
        self.label4.setPixmap(self.pix4)
        self.randx = random.randint(300, 1500)
        p = self.randx % 10
        self.merdevine1 = self.randx - p
        self.BoolBadzaMerdevine = False
        self.label4.setGeometry(self.merdevine1, 650, 90, 180)

        self.label5.setPixmap(self.pix5)
        self.randx2 = random.randint(300, 1500)
        p1 = self.randx2 % 10
        self.merdevine2 = self.randx2 - p1
        self.label5.setGeometry(self.merdevine2, 850, 90, 180)

        self.label6.setPixmap(self.pix6)
        self.label6.setGeometry(300, 460, 90, 180)

        self.label7.setPixmap(self.pix6)
        self.label7.setGeometry(1500, 460, 90, 180)

        self.label3.setPixmap(self.pix3)
        self.label3.setGeometry(300, 570, 85, 75)



        br += 1
        brLevel += 1
        font = QtGui.QFont()
        font.setPointSize(30)

        self.labelScore.setText(str(0))
        self.labelScore.setGeometry(1700, 202, 100, 100)
        self.labelScore.setFont(font)

        self.lives1 = 3
        self.labelLifes.setText(str(br))
        self.labelLifes.setGeometry(1700, 162, 100, 100)
        self.labelLifes.setFont(font)

        font.setPointSize(20)
        self.labelLevel.setText(str(brLevel))
        self.labelLevel.setGeometry(300, 125, 100, 100)
        self.labelLevel.setFont(font)

        self.pBar.setGeometry(140, 250, 300, 30)

        self.setWindowTitle('Popeye')
        self.show()
        self.labelforce.setPixmap(self.pixForce)
        self.timerP1.start(12000)
        self.timerP1.timeout.connect(self.timer_func)

    def progressing(self):
        self.step += 1
        self.pBar.setValue(self.step)
        if self.step == 100:
            self.level_no += 1
            self.step = 0
            self.pbar.setValue(self.step)
            self.labelLevel.setText(str(self.lev) + str(self.level_no))

    def keyPressEvent(self, event):
        a = event.key()
        self.key_notifier.add_key(a)
        if (self.brojIgracaJedan == False):
            b = event.key()
            self.key_notifier2.add_key(b)

    def keyReleaseEvent(self, event):
        a = event.key()
        self.key_notifier.rem_key(a)
        if (self.brojIgracaJedan == False):
            b = event.key()
            self.key_notifier2.rem_key(b)

    def __update_position__(self, key):
        rec1 = self.label1.geometry()
        """"
        if rec1.x() >= self.labelforce.x() - 10 and rec1.x() <= self.labelforce.x() + 10 and rec1.y() >= 755 and rec1.y() <= 785:
            self.hitF = True
            self.labelforce.hide()
            self.timerP1.start()
        """
        if isHit(self.label1, self.labelforce):
            self.hitF = True
            self.labelforce.hide()
            self.labelforce.setGeometry(-10, -10, 72, 56)
            self.timerP1.start()

        if key == Qt.Key_Right or key == Qt.Key_Left:
            if rec1.y() < 950 and rec1.y() >= 775:
                return
            elif (rec1.y() < 760 and rec1.y() >= 575):
                return

        if (key == Qt.Key_Down or key == Qt.Key_Up):
            if rec1.y() < 950 and rec1.y() >= 775:
                self.bounds = True
            elif (rec1.y() < 760 and rec1.y() >= 575):
                self.bounds = True
            else:
                self.bounds = False

        if ((rec1.x() >= 270 and rec1.x() <= 300) and (rec1.y() >= 755 and rec1.y() <= 775)):
            self.hitLeftUpStairs = True
            self.hitLeftUpStairsTop = False
        if ((rec1.x() >= 70 and rec1.x() <= 100) and (rec1.y() >= 540 and rec1.y() <= 575)):
            self.hitLeftUpStairsTop = True
            self.hitLeftUpStairs = False
        if ((rec1.x() >= 1570 and rec1.x() <= 1630) and (rec1.y() >= 755 and rec1.y() <= 775)):
            self.hitRightUpStairs = True
            self.hitRightUpStairsTop = False
        if ((rec1.x() >= 1770 and rec1.x() <= 1820) and (rec1.y() >= 555 and rec1.y() <= 575)):
            self.hitRightUpStairsTop = True
            self.hitRightUpStairs = False
        if ((rec1.x() >= 270 and rec1.x() <= 300) and (rec1.y() >= 950 and rec1.y() <= 965)):
            self.hitLeftDownStairs = True
            self.hitLeftDownStairsTop = False
        if ((rec1.x() >= 80 and rec1.x() <= 110) and (rec1.y() >= 755 and rec1.y() <= 775)):
            self.hitLeftDownStairsTop = True
            self.hitLeftDownStairs = False
        if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() > 950 and rec1.y() <= 965)):
            self.hitRightDownStairs = True
            self.hitRightDownStairsTop = False
        if ((rec1.x() >= 1760 and rec1.x() <= 1820) and (rec1.y() >= 755 and rec1.y() <= 775)):
            self.hitRightDownStairsTop = True
            self.hitRightDownStairs = False

        if key == Qt.Key_Right:
            if ((rec1.x() >= 270 and rec1.x() <= 290) and (rec1.y() >= 755 and rec1.y() <= 770)):
                self.hitLeftUpStairs = True
            else:
                self.hitLeftUpStairs = False
            if ((rec1.x() >= 80 and rec1.x() <= 100) and (rec1.y() >= 540 and rec1.y() <= 575)):
                self.hitLeftUpStairsTop = True
            else:
                self.hitLeftUpStairsTop = False
            if ((rec1.x() >= 1780 and rec1.x() <= 1820) and (rec1.y() >= 540 and rec1.y() <= 570)):
                self.hitRightUpStairsTop = True
            else:
                self.hitRightUpStairsTop = False
            if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() >= 755 and rec1.y() <= 770)):
                self.hitRightUpStairs = True
            else:
                self.hitRightUpStairs = False
            if ((rec1.x() >= 270 and rec1.x() <= 290) and (rec1.y() >= 950 and rec1.y() <= 965)):
                self.hitLeftDownStairs = True
            else:
                self.hitLeftDownStairs = False
            if ((rec1.x() >= 80 and rec1.x() <= 110) and (rec1.y() >= 755 and rec1.y() <= 770)):
                self.hitLeftDownStairsTop = True
            else:
                self.hitLeftDownStairsTop = False
            if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() >= 950 and rec1.y() <= 965)):
                self.hitRightDownStairs = True
            else:
                self.hitRightDownStairs = False
            if ((rec1.x() >= 1760 and rec1.x() <= 1820) and (rec1.y() >= 755 and rec1.y() <= 770)):
                self.hitRightDownStairsTop = True
            else:
                self.hitRightDownStairsTop = False

            if (rec1.x() < 1800 and (rec1.y() <= 960 and rec1.y() > 935) or (rec1.y() > 755 and rec1.y() < 780) or (
                    rec1.y() > 550 and rec1.y() < 575) or (
                    (rec1.y() > 371 and rec1.y() < 390) and (rec1.x() < 450 or rec1.x() >= 1400))):
                self.label1.setGeometry(rec1.x() + self.popeyeStep, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            if (rec1.y() <= 953):

                if (self.hitLeftUpStairs == False and self.hitLeftUpStairsTop == True):
                    self.label1.setGeometry(rec1.x() + self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.hitLeftDownStairs == False and self.hitLeftDownStairsTop == True):
                    self.label1.setGeometry(rec1.x() + self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.hitRightUpStairs == False and self.hitRightUpStairsTop == True):
                    self.label1.setGeometry(rec1.x() - self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.hitRightDownStairs == False and self.hitRightDownStairsTop == True):
                    self.label1.setGeometry(rec1.x() - self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.bounds == True and (
                        self.hitLeftUpStairs == True or self.hitLeftUpStairsTop == True or self.hitLeftDownStairs == True or self.hitLeftDownStairsTop == True
                )):
                    self.label1.setGeometry(rec1.x() + self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.bounds == True and (
                        self.hitRightDownStairsTop == True or self.hitRightDownStairs == True or self.hitRightUpStairs == True or self.hitRightUpStairsTop == True
                )):
                    self.label1.setGeometry(rec1.x() - self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())

                if (rec1.y() < 947 and rec1.y() <= 760 and (
                        rec1.x() > self.merdevine1 and rec1.x() < self.merdevine1 + 50) and rec1.y() >= 380):
                    self.label1.setGeometry(rec1.x(), rec1.y() + self.popeyeStep, rec1.width(), rec1.height())
                if (rec1.y() > 750 and (
                        rec1.x() > self.merdevine2 and rec1.x() < self.merdevine2 + 50) and rec1.y() <= 950):
                    self.label1.setGeometry(rec1.x(), rec1.y() + self.popeyeStep, rec1.width(), rec1.height())
                if ((rec1.x() <= 1530 and rec1.x() >= 1500) and (rec1.y() <= 560 and rec1.y() >= 370)):
                    self.label1.setGeometry(rec1.x(), rec1.y() + self.popeyeStep, rec1.width(), rec1.height())
                if ((rec1.x() <= 330 and rec1.x() >= 300) and (rec1.y() <= 560 and rec1.y() >= 370)):
                    self.label1.setGeometry(rec1.x(), rec1.y() + self.popeyeStep, rec1.width(), rec1.height())

        elif key == Qt.Key_Up:
            if (self.bounds == True and (
                    self.hitLeftUpStairs == True or self.hitLeftUpStairsTop == True or self.hitLeftDownStairs == True or self.hitLeftDownStairsTop == True
            )):
                self.label1.setGeometry(rec1.x() - self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())

            if (self.bounds == True and (
                    self.hitRightDownStairsTop == True or self.hitRightDownStairs == True or self.hitRightUpStairs == True or self.hitRightUpStairsTop == True
            )):
                self.label1.setGeometry(rec1.x() + self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())

            if (self.hitLeftUpStairs == True and self.hitLeftUpStairsTop == False):
                self.label1.setGeometry(rec1.x() - self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())
            if (self.hitLeftDownStairs == True and self.hitLeftDownStairsTop == False):
                self.label1.setGeometry(rec1.x() - self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())
            if (self.hitRightUpStairs == True and self.hitRightUpStairsTop == False):
                self.label1.setGeometry(rec1.x() + self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())
            if (self.hitRightDownStairs == True and self.hitRightDownStairsTop == False):
                self.label1.setGeometry(rec1.x() + self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())
            if (rec1.y() >= 570 and (
                    rec1.x() > self.merdevine1 and rec1.x() < self.merdevine1 + 50) and rec1.y() <= 780):
                self.label1.setGeometry(rec1.x(), rec1.y() - self.popeyeStep, rec1.width(), rec1.height())
            if (rec1.y() > 50 and (
                    rec1.x() > self.merdevine2 and rec1.x() < self.merdevine2 + 50) and rec1.y() >= 780 and rec1.y() <= 960):
                self.label1.setGeometry(rec1.x(), rec1.y() - self.popeyeStep, rec1.width(), rec1.height())
            if ((rec1.x() <= 1530 and rec1.x() >= 1500) and (rec1.y() <= 580 and rec1.y() >= 385)):
                self.label1.setGeometry(rec1.x(), rec1.y() - self.popeyeStep, rec1.width(), rec1.height())
            if ((rec1.x() <= 330 and rec1.x() >= 300) and (rec1.y() <= 580 and rec1.y() >= 385)):
                self.label1.setGeometry(rec1.x(), rec1.y() - self.popeyeStep, rec1.width(), rec1.height())

        elif key == Qt.Key_Left:
            if ((rec1.x() >= 270 and rec1.x() <= 290) and (rec1.y() >= 755 and rec1.y() <= 770)):
                self.hitLeftUpStairs = True
            else:
                self.hitLeftUpStairs = False
            if ((rec1.x() >= 80 and rec1.x() <= 110) and (rec1.y() >= 540 and rec1.y() <= 575)):
                self.hitLeftUpStairsTop = True
            else:
                self.hitLeftUpStairsTop = False
            if ((rec1.x() >= 1780 and rec1.x() <= 1820) and (rec1.y() >= 540 and rec1.y() <= 570)):
                self.hitRightUpStairsTop = True
            else:
                self.hitRightUpStairsTop = False
            if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() >= 755 and rec1.y() <= 775)):
                self.hitRightUpStairs = True
            else:
                self.hitRightUpStairs = False
            if ((rec1.x() >= 270 and rec1.x() <= 290) and (rec1.y() >= 950 and rec1.y() <= 965)):
                self.hitLeftDownStairs = True
            else:
                self.hitLeftDownStairs = False
            if ((rec1.x() >= 80 and rec1.x() <= 110) and (rec1.y() >= 755 and rec1.y() <= 770)):
                self.hitLeftDownStairsTop = True
            else:
                self.hitLeftDownStairsTop = False
            if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() >= 950 and rec1.y() <= 965)):
                self.hitRightDownStairs = True
            else:
                self.hitRightDownStairs = False
            if ((rec1.x() >= 1760 and rec1.x() <= 1820) and (rec1.y() >= 755 and rec1.y() <= 775)):
                self.hitRightDownStairsTop = True
            else:
                self.hitRightDownStairsTop = False
            if (rec1.x() > 50 and ((rec1.y() <= 960 and rec1.y() > 935) or (rec1.y() > 755 and rec1.y() < 780) or (
                    rec1.y() > 550 and rec1.y() < 575) or ((rec1.y() > 371 and rec1.y() < 390) and (
                    rec1.x() <= 450 or rec1.x() >= 1450)))):
                self.label1.setGeometry(rec1.x() - self.popeyeStep, rec1.y(), rec1.width(), rec1.height())

    def __update_position2__(self, key):
        rec1 = self.label11.geometry()

        if (rec1.x() >= self.labelforce.x() - 10 and rec1.x() <= self.labelforce.x() + 10 and rec1.y() >= 755 and rec1.y() <= 785):
            self.hitF = True
            self.labelforce.hide()
            self.timerP1.start()

        if key == Qt.Key_D or key == Qt.Key_A:
            if rec1.y() < 950 and rec1.y() >= 775:
                return
            elif (rec1.y() < 760 and rec1.y() >= 575):
                return

        if (key == Qt.Key_S or key == Qt.Key_W):
            if rec1.y() < 950 and rec1.y() >= 775:
                self.bounds = True
            elif (rec1.y() < 760 and rec1.y() >= 575):
                self.bounds = True
            else:
                self.bounds = False

        if ((rec1.x() >= 270 and rec1.x() <= 300) and (rec1.y() >= 755 and rec1.y() <= 775)):
            self.hitLeftUpStairs2 = True
            self.hitLeftUpStairsTop2 = False
        if ((rec1.x() >= 70 and rec1.x() <= 100) and (rec1.y() >= 540 and rec1.y() <= 575)):
            self.hitLeftUpStairsTop2 = True
            self.hitLeftUpStairs2 = False
        if ((rec1.x() >= 1570 and rec1.x() <= 1630) and (rec1.y() >= 755 and rec1.y() <= 775)):
            self.hitRightUpStairs2 = True
            self.hitRightUpStairsTop2 = False
        if ((rec1.x() >= 1770 and rec1.x() <= 1820) and (rec1.y() >= 555 and rec1.y() <= 575)):
            self.hitRightUpStairsTop2 = True
            self.hitRightUpStairs2 = False
        if ((rec1.x() >= 270 and rec1.x() <= 300) and (rec1.y() >= 950 and rec1.y() <= 965)):
            self.hitLeftDownStairs2 = True
            self.hitLeftDownStairsTop2 = False
        if ((rec1.x() >= 80 and rec1.x() <= 110) and (rec1.y() >= 755 and rec1.y() <= 775)):
            self.hitLeftDownStairsTop2 = True
            self.hitLeftDownStairs2 = False
        if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() > 950 and rec1.y() <= 965)):
            self.hitRightDownStairs2 = True
            self.hitRightDownStairsTop2 = False
        if ((rec1.x() >= 1760 and rec1.x() <= 1820) and (rec1.y() >= 755 and rec1.y() <= 775)):
            self.hitRightDownStairsTop2 = True
            self.hitRightDownStairs2 = False

        if key == Qt.Key_D:
            if (rec1.x() <= 1780):
                if ((rec1.x() >= 270 and rec1.x() <= 290) and (rec1.y() >= 755 and rec1.y() <= 770)):
                    self.hitLeftUpStairs2 = True
                else:
                    self.hitLeftUpStairs2 = False
                if ((rec1.x() >= 80 and rec1.x() <= 100) and (rec1.y() >= 540 and rec1.y() <= 575)):
                    self.hitLeftUpStairsTop2 = True
                else:
                    self.hitLeftUpStairsTop2 = False
                if ((rec1.x() >= 1780 and rec1.x() <= 1820) and (rec1.y() >= 540 and rec1.y() <= 570)):
                    self.hitRightUpStairsTop2 = True
                else:
                    self.hitRightUpStairsTop2 = False
                if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() >= 755 and rec1.y() <= 770)):
                    self.hitRightUpStairs2 = True
                else:
                    self.hitRightUpStairs2 = False
                if ((rec1.x() >= 270 and rec1.x() <= 290) and (rec1.y() >= 950 and rec1.y() <= 965)):
                    self.hitLeftDownStairs2 = True
                else:
                    self.hitLeftDownStairs2 = False
                if ((rec1.x() >= 80 and rec1.x() <= 110) and (rec1.y() >= 755 and rec1.y() <= 770)):
                    self.hitLeftDownStairsTop2 = True
                else:
                    self.hitLeftDownStairsTop2 = False
                if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() >= 950 and rec1.y() <= 965)):
                    self.hitRightDownStairs2 = True
                else:
                    self.hitRightDownStairs2 = False
                if ((rec1.x() >= 1760 and rec1.x() <= 1820) and (rec1.y() >= 755 and rec1.y() <= 770)):
                    self.hitRightDownStairsTop2 = True
                else:
                    self.hitRightDownStairsTop2 = False

                if (rec1.x() < 1800 and (rec1.y() <= 960 and rec1.y() > 935) or (rec1.y() > 755 and rec1.y() < 780) or (
                                rec1.y() > 550 and rec1.y() < 575) or (
                            (rec1.y() > 371 and rec1.y() < 390) and (rec1.x() < 450 or rec1.x() >= 1400))):
                    self.label11.setGeometry(rec1.x() + self.popeyeStep, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_S:
            if (rec1.y() <= 953):

                if (self.hitLeftUpStairs2 == False and self.hitLeftUpStairsTop2 == True):
                    self.label11.setGeometry(rec1.x() + self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.hitLeftDownStairs2 == False and self.hitLeftDownStairsTop2 == True):
                    self.label11.setGeometry(rec1.x() + self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.hitRightUpStairs2 == False and self.hitRightUpStairsTop2 == True):
                    self.label11.setGeometry(rec1.x() - self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.hitRightDownStairs2 == False and self.hitRightDownStairsTop2 == True):
                    self.label11.setGeometry(rec1.x() - self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.bounds == True and (
                                self.hitLeftUpStairs2 == True or self.hitLeftUpStairsTop2 == True or self.hitLeftDownStairs2 == True or self.hitLeftDownStairsTop2 == True
                                )):
                    self.label11.setGeometry(rec1.x() + self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())
                if (self.bounds == True and (
                                        self.hitRightDownStairsTop2 == True or self.hitRightDownStairs2 == True or self.hitRightUpStairs2 == True or self.hitRightUpStairsTop2 == True
                )):
                    self.label11.setGeometry(rec1.x() - self.popeyeStep, rec1.y() + self.popeyeStep, rec1.width(),
                                            rec1.height())

                if (rec1.y() < 947 and rec1.y() <= 760 and (
                                rec1.x() > self.merdevine1 and rec1.x() < self.merdevine1 + 50) and rec1.y() >= 380):
                    self.label11.setGeometry(rec1.x(), rec1.y() + self.popeyeStep, rec1.width(), rec1.height())
                if (rec1.y() > 750 and (
                                rec1.x() > self.merdevine2 and rec1.x() < self.merdevine2 + 50) and rec1.y() <= 950):
                    self.label11.setGeometry(rec1.x(), rec1.y() + self.popeyeStep, rec1.width(), rec1.height())
                if ((rec1.x() <= 1530 and rec1.x() >= 1500) and (rec1.y() <= 560 and rec1.y() >= 370)):
                    self.label11.setGeometry(rec1.x(), rec1.y() + self.popeyeStep, rec1.width(), rec1.height())
                if ((rec1.x() <= 330 and rec1.x() >= 300) and (rec1.y() <= 560 and rec1.y() >= 370)):
                    self.label11.setGeometry(rec1.x(), rec1.y() + self.popeyeStep, rec1.width(), rec1.height())

        elif key == Qt.Key_W:
            if (self.bounds == True and (
                                    self.hitLeftUpStairs2 == True or self.hitLeftUpStairsTop2 == True or self.hitLeftDownStairs2 == True or self.hitLeftDownStairsTop2 == True
            )):
                self.label11.setGeometry(rec1.x() - self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())

            if (self.bounds == True and (
                                    self.hitRightDownStairsTop2 == True or self.hitRightDownStairs2 == True or self.hitRightUpStairs2 == True or self.hitRightUpStairsTop2 == True
            )):
                self.label11.setGeometry(rec1.x() + self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())

            if (self.hitLeftUpStairs2 == True and self.hitLeftUpStairsTop2 == False):
                self.label11.setGeometry(rec1.x() - self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())
            if (self.hitLeftDownStairs2 == True and self.hitLeftDownStairsTop2 == False):
                self.label11.setGeometry(rec1.x() - self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())
            if (self.hitRightUpStairs2 == True and self.hitRightUpStairsTop2 == False):
                self.label11.setGeometry(rec1.x() + self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())
            if (self.hitRightDownStairs2 == True and self.hitRightDownStairsTop2 == False):
                self.label11.setGeometry(rec1.x() + self.popeyeStep, rec1.y() - self.popeyeStep, rec1.width(),
                                        rec1.height())
            if (rec1.y() >= 570 and (
                            rec1.x() > self.merdevine1 and rec1.x() < self.merdevine1 + 50) and rec1.y() <= 780):
                self.label11.setGeometry(rec1.x(), rec1.y() - self.popeyeStep, rec1.width(), rec1.height())
            if (rec1.y() > 50 and (
                            rec1.x() > self.merdevine2 and rec1.x() < self.merdevine2 + 50) and rec1.y() >= 780 and rec1.y() <= 960):
                self.label11.setGeometry(rec1.x(), rec1.y() - self.popeyeStep, rec1.width(), rec1.height())
            if ((rec1.x() <= 1530 and rec1.x() >= 1500) and (rec1.y() <= 580 and rec1.y() >= 385)):
                self.label11.setGeometry(rec1.x(), rec1.y() - self.popeyeStep, rec1.width(), rec1.height())
            if ((rec1.x() <= 330 and rec1.x() >= 300) and (rec1.y() <= 580 and rec1.y() >= 385)):
                self.label11.setGeometry(rec1.x(), rec1.y() - self.popeyeStep, rec1.width(), rec1.height())

        elif key == Qt.Key_A:
            if ((rec1.x() >= 270 and rec1.x() <= 290) and (rec1.y() >= 755 and rec1.y() <= 770)):
                self.hitLeftUpStairs2 = True
            else:
                self.hitLeftUpStairs2 = False
            if ((rec1.x() >= 80 and rec1.x() <= 110) and (rec1.y() >= 540 and rec1.y() <= 575)):
                self.hitLeftUpStairsTop2 = True
            else:
                self.hitLeftUpStairsTop2 = False
            if ((rec1.x() >= 1780 and rec1.x() <= 1820) and (rec1.y() >= 540 and rec1.y() <= 570)):
                self.hitRightUpStairsTop2 = True
            else:
                self.hitRightUpStairsTop2 = False
            if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() >= 755 and rec1.y() <= 775)):
                self.hitRightUpStairs2 = True
            else:
                self.hitRightUpStairs2 = False
            if ((rec1.x() >= 270 and rec1.x() <= 290) and (rec1.y() >= 950 and rec1.y() <= 965)):
                self.hitLeftDownStairs2 = True
            else:
                self.hitLeftDownStairs2 = False
            if ((rec1.x() >= 80 and rec1.x() <= 110) and (rec1.y() >= 755 and rec1.y() <= 770)):
                self.hitLeftDownStairsTop2 = True
            else:
                self.hitLeftDownStairsTop2 = False
            if ((rec1.x() >= 1570 and rec1.x() <= 1610) and (rec1.y() >= 950 and rec1.y() <= 965)):
                self.hitRightDownStairs2 = True
            else:
                self.hitRightDownStairs2 = False
            if ((rec1.x() >= 1760 and rec1.x() <= 1820) and (rec1.y() >= 755 and rec1.y() <= 775)):
                self.hitRightDownStairsTop2 = True
            else:
                self.hitRightDownStairsTop2 = False
            if (rec1.x() > 50 and ((rec1.y() <= 960 and rec1.y() > 935) or (rec1.y() > 755 and rec1.y() < 780) or (
                            rec1.y() > 550 and rec1.y() < 575) or (
                (rec1.y() > 371 and rec1.y() < 390) and (rec1.x() <= 450 or rec1.x() >= 1450)))):
                self.label11.setGeometry(rec1.x() - self.popeyeStep, rec1.y(), rec1.width(), rec1.height())

    def moveOlive(self):
        rec2 = self.label2.geometry()

        if rec2.x() == 1300:
            self.hitSide = True
        elif rec2.x() == 550:
            self.hitSide = False

        a = randint(0, 1000)
        if a % 125 == 0:
            heart = QLabel(self)
            heart.setPixmap(self.pixHeart)
            heart.setGeometry(rec2.x(), rec2.y() + 50, 30, 26)
            self.hearts.append(heart)
            self.hearts[len(self.hearts) - 1].setPixmap(self.pixHeart)
            self.hearts[len(self.hearts) - 1].setGeometry(rec2.x(), rec2.y(), 30, 26)
            self.hearts[len(self.hearts) - 1].show()

        if self.hitSide:
            self.label2.setGeometry(rec2.x() - 10, rec2.y() + 0, rec2.width(), rec2.height())
        else:
            self.label2.setGeometry(rec2.x() + 10, rec2.y() + 0, rec2.width(), rec2.height())

    def generateHeart(self):
        for heart in self.hearts:
            if isHit(self.label1, heart):
                self.poeni1 += 1
                self.labelScore.setText(str(self.poeni1))
                heart.hide()
                heart.setGeometry(0, 0, 30, 28)
                self.hearts.remove(heart)
            else:
                rec5 = heart.geometry()
                heart.setGeometry(rec5.x(), rec5.y() + 4, rec5.width(), rec5.height())

    def generateBombs(self):
        if not self.q.empty():
            x = self.q.get()
            bomb = QLabel(self)
            self.bombs.append(bomb)
            self.bombs[len(self.bombs) - 1].setPixmap(self.pixBomb)
            self.bombs[len(self.bombs) - 1].setGeometry(x, 10, 30, 26)
            self.bombs[len(self.bombs) - 1].show()

    def moveBombs(self):
        for bomb in self.bombs:
            rec = bomb.geometry()
            bomb.setGeometry(rec.x(), rec.y() + 6, rec.width(), rec.height())
            if isHit(bomb, self.label1):
                self.lives1 -= 1
                self.labelLifes.setText(str(self.lives1))
                bomb.hide()
                bomb.setGeometry(0, 0, rec.width(), rec.height())
                self.bombs.remove(bomb)

    def moveBadzo(self):
        # if(self.hitSide):
        #   rec3 = self.label3.geometry()
        # elif(self.hitSide==False):
        #  rec3 = self.label30.geometry()
        rec3 = self.label3.geometry()

        if self.hitF:
            if not self.zaustavio:
                self.badzoStop.put(1)
                self.zaustavio = True
                return
            else:
                if self.badzoStart.empty():
                    return
                else:
                    a = self.badzoStart.get()
                    self.hitF = False
                self.zaustavio = False

        if (self.sprat == 1):

            self.boolSkok += 1
            if (rec3.x() == 1500):
                self.hitSide2 = True
                self.LadderUPBadzo = self.BoolBadzaMerdevine
                self.boolSkok += 1
            elif (rec3.x() == self.merdevine1):  # or self.boolSkok==True):
                self.LadderDownBadzo = self.BoolBadzaMerdevine
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


        elif (self.sprat == 2):
            if (rec3.x() == 1500):
                self.hitSide2 = True
            elif (rec3.x() == self.merdevine2):  # or self.boolSkok == True):
                self.LadderDownBadzo = self.BoolBadzaMerdevine
            elif (rec3.x() == self.merdevine1):
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
                # elif (rec3.x() == self.merdevine2):
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
            elif (rec3.x() == 300 or rec3.x() == 1500):
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

    def timer_func(self):
        x = random.randint(300, 1500)
        self.labelforce.setGeometry(x, 780, 72, 56)
        self.labelforce.show()
        self.timerP2.start(10000)
        self.timerP2.timeout.connect(self.hide_force)

    def hide_force(self):
        self.labelforce.hide()
        self.labelforce.destroy()

    def closeEvent(self, event):
        self.key_notifier.die()
        self.key_notifier2.die()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
