import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import Login_Win
from newAcc_view import newAccWin
from main import MainWin
import pymysql

class loginWin(QMainWindow,Login_Win.Ui_LoginWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.account=newAccWin()
        self.new_btn.clicked.connect(self.new_Clicked)
        self.login_btn.clicked.connect(self.login_Clicked)
        self.bgLabel.setStyleSheet('image:url(./views_img/login.png);')



    def new_Clicked(self):
        self.account.show()

    def login_Clicked(self):
        self.userid = self.id_lld.text()
        self.pwd = self.pass_lld.text()
        self.main1 = MainWin(self.userid)
        conn = pymysql.connect(host='localhost', user='root', password='love6220',
                               db='userinfo', charset='utf8')
        curs = conn.cursor()
        sql="select * from users where id=%s and passwd=%s"
        data=curs.execute(sql, (self.userid, self.pwd))
        if(len(curs.fetchall())>0):
            self.res_lbl.setText("")
            self.main1.show()
        else:
            self.res_lbl.setText("로그인이 실패했습니다.")



if __name__=="__main__":
    app = QApplication(sys.argv)
    m_w = loginWin()
    m_w.show()
    sys.exit(app.exec_())
