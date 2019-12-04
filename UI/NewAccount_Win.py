# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewAccount_Win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newAccountWin(object):
    def setupUi(self, newAccountWin):
        newAccountWin.setObjectName("newAccountWin")
        newAccountWin.resize(1024, 1024)
        newAccountWin.setMinimumSize(QtCore.QSize(1024, 1024))
        newAccountWin.setMaximumSize(QtCore.QSize(1024, 1024))
        newAccountWin.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(newAccountWin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 640, 91, 61))
        self.label.setStyleSheet("font: 16pt \"210 Namoogulrim\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 710, 181, 61))
        self.label_2.setStyleSheet("font: 16pt \"210 Namoogulrim\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 540, 311, 61))
        self.label_3.setStyleSheet("\n"
"font: 24pt \"나눔스퀘어 Bold\";\n"
"color: rgb(107, 45, 126);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_btn.setGeometry(QtCore.QRect(440, 840, 161, 61))
        self.create_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 45, 126);\n"
"font: 20pt \"나눔스퀘어\";")
        self.create_btn.setObjectName("create_btn")
        self.id_nle = QtWidgets.QLineEdit(self.centralwidget)
        self.id_nle.setGeometry(QtCore.QRect(510, 650, 241, 41))
        self.id_nle.setStyleSheet("font: 12pt \"210 Namoogulrim\";")
        self.id_nle.setText("")
        self.id_nle.setObjectName("id_nle")
        self.pass_nle = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_nle.setGeometry(QtCore.QRect(510, 720, 241, 41))
        self.pass_nle.setStyleSheet("font: 12pt \"210 Namoogulrim\";")
        self.pass_nle.setObjectName("pass_nle")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 790, 281, 31))
        self.label_4.setStyleSheet("font: 12pt \"나눔스퀘어\";")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 1024, 1024))
        self.bgLabel.setMinimumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setMaximumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setText("")
        self.bgLabel.setObjectName("bgLabel")
        self.bgLabel.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.create_btn.raise_()
        self.id_nle.raise_()
        self.pass_nle.raise_()
        self.label_4.raise_()
        newAccountWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(newAccountWin)
        QtCore.QMetaObject.connectSlotsByName(newAccountWin)

    def retranslateUi(self, newAccountWin):
        _translate = QtCore.QCoreApplication.translate
        newAccountWin.setWindowTitle(_translate("newAccountWin", "New Account"))
        self.label.setText(_translate("newAccountWin", "ID"))
        self.label_2.setText(_translate("newAccountWin", "PASSWORD"))
        self.label_3.setText(_translate("newAccountWin", "NEW ACCOUNT"))
        self.create_btn.setText(_translate("newAccountWin", "CREATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newAccountWin = QtWidgets.QMainWindow()
    ui = Ui_newAccountWin()
    ui.setupUi(newAccountWin)
    newAccountWin.show()
    sys.exit(app.exec_())

