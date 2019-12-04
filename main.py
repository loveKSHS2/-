import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import Main_Win
from search_view import MySearchWin
from recommend_view import RecWin
from his_view import HisWin

class MainWin(QMainWindow,Main_Win.Ui_MainWindow):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.search_sec=MySearchWin(id)
        self.rec_sec=RecWin()
        self.history=HisWin(id)
        self.bgLabel.setStyleSheet('image:url(./views_img/main.png);')
        self.search_btn.setStyleSheet('image:url(./views_img/serBtn.png); border:0px;')
        self.rend_btn.setStyleSheet('image:url(./views_img/recBtn.png); border:0px;')
        self.his_btn.setStyleSheet('image:url(./views_img/hisBtn.png); border:0px;')
        self.search_btn.clicked.connect(self.search_Clicked)
        self.rend_btn.clicked.connect(self.rend_Clicked)
        self.his_btn.clicked.connect(self.his_Clicked)

    def his_Clicked(self):
        self.history.show()

    def search_Clicked(self):
        self.search_sec.show()

    def rend_Clicked(self):
        self.rec_sec.show()



if __name__=="__main__":
    app = QApplication(sys.argv)
    m_w = MainWin()
    m_w.show()
    sys.exit(app.exec_())
