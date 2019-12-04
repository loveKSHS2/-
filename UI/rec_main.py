# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rec_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 1024)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 1024))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 1024))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../rec/venv/logo_only.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(530, 460, 30, 40))
        self.btn3.setMinimumSize(QtCore.QSize(30, 40))
        self.btn3.setMaximumSize(QtCore.QSize(30, 40))
        self.btn3.setText("")
        self.btn3.setObjectName("btn3")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(110, 430, 30, 40))
        self.btn1.setMinimumSize(QtCore.QSize(30, 40))
        self.btn1.setMaximumSize(QtCore.QSize(30, 40))
        self.btn1.setText("")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(430, 540, 30, 40))
        self.btn2.setMinimumSize(QtCore.QSize(30, 40))
        self.btn2.setMaximumSize(QtCore.QSize(30, 40))
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(810, 500, 30, 40))
        self.btn4.setMinimumSize(QtCore.QSize(30, 40))
        self.btn4.setMaximumSize(QtCore.QSize(30, 40))
        self.btn4.setText("")
        self.btn4.setObjectName("btn4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 1024))
        self.label.setMinimumSize(QtCore.QSize(1024, 1024))
        self.label.setMaximumSize(QtCore.QSize(1024, 1024))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.btn3.raise_()
        self.btn1.raise_()
        self.btn2.raise_()
        self.btn4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choose the place"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

