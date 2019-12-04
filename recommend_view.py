import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import rec_main
from recDetail_view import RecDetailWin

#rec_main_UI = './rec_main.ui'

class RecWin(QMainWindow,rec_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #uic.loadUi(rec_main_UI, self)

        self.rec_btn()
        self.label.setStyleSheet('image:url(./views_img/rec_main_bg.png);')

        #self.btnNum = [False,False,False,False]

        self.btn1.clicked.connect(lambda: self.next_btn(1))
        self.btn2.clicked.connect(lambda: self.next_btn(2))
        self.btn3.clicked.connect(lambda: self.next_btn(3))
        self.btn4.clicked.connect(lambda: self.next_btn(4))
        #self.btn2.clicked.connect(self.next_btn2())
        #self.btn3.clicked.connect(self.next_btn3())
        #self.btn4.clicked.connect(self.next_btn4())

    def next_btn(self, val):
        self.detail = RecDetailWin(val)
        self.detail.show()

    def rec_btn(self):
        #button iagme setting
        #self.chinaBtn.setStyleSheet('image:url(./pin1.png); border:0px;')

        self.btn1.setStyleSheet('''
        QPushButton{image:url(./views_img/pin1.png); border:0px;}
        QPushButton:hover{image:url(./views_img/pin2.png); border:0px;}
        ''')

        self.btn2.setStyleSheet('''
                QPushButton{image:url(./views_img/pin1.png); border:0px;}
                QPushButton:hover{image:url(./views_img/pin2.png); border:0px;}
                ''')

        self.btn3.setStyleSheet('''
                QPushButton{image:url(./views_img/pin1.png); border:0px;}
                QPushButton:hover{image:url(./views_img/pin2.png); border:0px;}
                ''')

        self.btn4.setStyleSheet('''
                QPushButton{image:url(./views_img/pin1.png); border:0px;}
                QPushButton:hover{image:url(./views_img/pin2.png); border:0px;}
                ''')

if __name__=="__main__":
    app = QApplication(sys.argv)
    m_w = RecWin()
    m_w.show()
    sys.exit(app.exec_())