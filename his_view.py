import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import History_Win
import pymysql

class HisWin(QMainWindow, History_Win.Ui_HistoryWin):
    def __init__(self,id):
        super().__init__()
        self.setupUi(self)
        self.sql_result(id)
        self.cnt=-1
        self.next_btn.clicked.connect(self.next_Clicked)
        self.prev_btn.clicked.connect(self.prev_Clicked)
        #self.bgLabel.setStyleSheet('image:url(./views_img/main.png);')

    def next_Clicked(self):
        self.length=len(self.paths)
        if self.length<=self.cnt or self.length==0:
            self.picss.setText("")
        else:
            self.pix = QPixmap(self.paths[self.cnt][1])
            self.pix = self.pix.scaled(400,400)
            self.picss.setPixmap(QPixmap(self.pix))
            self.pix1 = QPixmap(self.paths[self.cnt][2])
            self.pix1 = self.pix1.scaled(400, 400)
            self.result1.setPixmap(QPixmap(self.pix1))
            self.pix2 = QPixmap(self.paths[self.cnt][3])
            self.pix2 = self.pix2.scaled(400, 400)
            self.result2.setPixmap(QPixmap(self.pix2))
            self.pix3 = QPixmap(self.paths[self.cnt][4])
            self.pix3 = self.pix3.scaled(400, 400)
            self.result3.setPixmap(QPixmap(self.pix3))
            self.cnt += 1

    def prev_Clicked(self):
        self.length=len(self.paths)
        if 0>self.cnt or self.length==0:
            self.picss.setText("")
        else:
            self.pix = QPixmap(self.paths[self.cnt][1])
            self.pix = self.pix.scaled(400,400)
            self.picss.setPixmap(QPixmap(self.pix))
            self.pix1 = QPixmap(self.paths[self.cnt][2])
            self.pix1 = self.pix1.scaled(400, 400)
            self.result1.setPixmap(QPixmap(self.pix1))
            self.pix2 = QPixmap(self.paths[self.cnt][3])
            self.pix2 = self.pix2.scaled(400, 400)
            self.result2.setPixmap(QPixmap(self.pix2))
            self.pix3 = QPixmap(self.paths[self.cnt][4])
            self.pix3 = self.pix3.scaled(400, 400)
            self.result3.setPixmap(QPixmap(self.pix3))
            self.cnt -= 1




    def sql_result(self, uid):
        conn = pymysql.connect(host='localhost', user='root', password='love6220',
                               db='userinfo', charset='utf8')
        curs = conn.cursor()
        sql = "select * from userpaths where u_id=%s"
        data = curs.execute(sql, (uid))
        self.paths=curs.fetchall()






if __name__=="__main__":
    app = QApplication(sys.argv)
    m_w = HisWin()
    m_w.show()
    sys.exit(app.exec_())
