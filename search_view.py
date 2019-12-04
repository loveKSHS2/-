import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from UI import Search_Win
from result_view import MyResultWin


class MySearchWin(QMainWindow,Search_Win.Ui_SearchWin):
    def __init__(self, uid):
        self.id=uid
        super().__init__()
        self.setupUi(self)
        self.bgLabel.setStyleSheet('image:url(./views_img/ser_main_bg.png);')
        self.results_btn.clicked.connect(self.resultBtn_Clicked)
        self.open_btn.clicked.connect(self.openBtn_Clicked)


    def resultBtn_Clicked(self):
        self.selReg=self.region.currentText()
        self.third = MyResultWin(self.img_path, self.id,self.selReg)
        self.third.show()

    def openBtn_Clicked(self):
        fname = QFileDialog.getOpenFileName(self,'Open file')
        self.img_path = fname[0]
        self.pixmap=QPixmap(self.img_path)
        self.pixmap=self.pixmap.scaled(600,350)
        self.pics_lbl.setPixmap(QPixmap(self.pixmap))

        self.show()



if __name__=="__main__":
    app=QApplication(sys.argv)
    dig=MySearchWin()
    dig.show()
    sys.exit(app.exec_())
