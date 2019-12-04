# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWin(object):
    def setupUi(self, LoginWin):
        LoginWin.setObjectName("LoginWin")
        LoginWin.resize(1024, 1024)
        LoginWin.setMinimumSize(QtCore.QSize(1024, 1024))
        LoginWin.setMaximumSize(QtCore.QSize(1024, 1024))
        LoginWin.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LoginWin)
        self.centralwidget.setObjectName("centralwidget")
        self.id_lbl = QtWidgets.QLabel(self.centralwidget)
        self.id_lbl.setGeometry(QtCore.QRect(160, 660, 71, 91))
        self.id_lbl.setStyleSheet("font: 18pt \"나눔스퀘어\";\n"
"")
        self.id_lbl.setObjectName("id_lbl")
        self.pwd_lbl = QtWidgets.QLabel(self.centralwidget)
        self.pwd_lbl.setGeometry(QtCore.QRect(160, 720, 191, 91))
        self.pwd_lbl.setStyleSheet("font: 18pt \"나눔스퀘어\";")
        self.pwd_lbl.setObjectName("pwd_lbl")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(690, 680, 131, 111))
        self.login_btn.setStyleSheet("font: 18pt \"나눔스퀘어\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 45, 126);")
        self.login_btn.setObjectName("login_btn")
        self.res_lbl = QtWidgets.QLabel(self.centralwidget)
        self.res_lbl.setGeometry(QtCore.QRect(360, 630, 271, 31))
        self.res_lbl.setStyleSheet("font: 12pt \"나눔스퀘어\";")
        self.res_lbl.setText("")
        self.res_lbl.setObjectName("res_lbl")
        self.id_lld = QtWidgets.QLineEdit(self.centralwidget)
        self.id_lld.setGeometry(QtCore.QRect(350, 680, 291, 41))
        self.id_lld.setStyleSheet("font: 12pt \"210 Namoogulrim\";")
        self.id_lld.setText("")
        self.id_lld.setObjectName("id_lld")
        self.pass_lld = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_lld.setGeometry(QtCore.QRect(350, 740, 291, 41))
        self.pass_lld.setStyleSheet("font: 12pt \"210 Namoogulrim\";")
        self.pass_lld.setInputMask("")
        self.pass_lld.setText("")
        self.pass_lld.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lld.setObjectName("pass_lld")
        self.new_btn = QtWidgets.QPushButton(self.centralwidget)
        self.new_btn.setGeometry(QtCore.QRect(690, 810, 131, 31))
        self.new_btn.setStyleSheet("font: 10pt \"나눔스퀘어\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 45, 126);")
        self.new_btn.setObjectName("new_btn")
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 1024, 1024))
        self.bgLabel.setMinimumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setMaximumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setText("")
        self.bgLabel.setObjectName("bgLabel")
        self.bgLabel.raise_()
        self.id_lbl.raise_()
        self.pwd_lbl.raise_()
        self.login_btn.raise_()
        self.res_lbl.raise_()
        self.id_lld.raise_()
        self.pass_lld.raise_()
        self.new_btn.raise_()
        LoginWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWin)
        QtCore.QMetaObject.connectSlotsByName(LoginWin)

    def retranslateUi(self, LoginWin):
        _translate = QtCore.QCoreApplication.translate
        LoginWin.setWindowTitle(_translate("LoginWin", "Login"))
        self.id_lbl.setText(_translate("LoginWin", "ID"))
        self.pwd_lbl.setText(_translate("LoginWin", "PASSWORD"))
        self.login_btn.setText(_translate("LoginWin", "LOGIN"))
        self.new_btn.setText(_translate("LoginWin", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWin = QtWidgets.QMainWindow()
    ui = Ui_LoginWin()
    ui.setupUi(LoginWin)
    LoginWin.show()
    sys.exit(app.exec_())

