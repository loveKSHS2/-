import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import NewAccount_Win
import pymysql

class newAccWin(QMainWindow,NewAccount_Win.Ui_newAccountWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.create_btn.clicked.connect(self.create_Clicked)
        self.bgLabel.setStyleSheet('image:url(./views_img/sign.png);')

    def create_Clicked(self):
        self.n_id = self.id_nle.text()
        self.n_pass = self.pass_nle.text()
        conn = pymysql.connect(host='localhost', user='root', password='love6220',
                               db='userinfo', charset='utf8')
        curs = conn.cursor()
        sql = "INSERT INTO users(id, passwd) VALUES(%s, %s)"
        curs.execute(sql, (self.n_id, self.n_pass))
        conn.commit()
        self.label_4.setText("생성되었습니다.")



if __name__=="__main__":
    app = QApplication(sys.argv)
    m_w = newAccWin()
    m_w.show()
    sys.exit(app.exec_())
