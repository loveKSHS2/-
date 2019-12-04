# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'History_Win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HistoryWin(object):
    def setupUi(self, HistoryWin):
        HistoryWin.setObjectName("HistoryWin")
        HistoryWin.resize(1024, 1024)
        HistoryWin.setMinimumSize(QtCore.QSize(1024, 1024))
        HistoryWin.setMaximumSize(QtCore.QSize(1024, 1024))
        self.centralwidget = QtWidgets.QWidget(HistoryWin)
        self.centralwidget.setObjectName("centralwidget")
        self.picss = QtWidgets.QLabel(self.centralwidget)
        self.picss.setGeometry(QtCore.QRect(280, 90, 400, 400))
        self.picss.setMinimumSize(QtCore.QSize(400, 400))
        self.picss.setMaximumSize(QtCore.QSize(400, 400))
        self.picss.setText("")
        self.picss.setObjectName("picss")
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(720, 430, 121, 71))
        self.next_btn.setStyleSheet("font: 14pt \"나눔스퀘어\";\n"
"color: rgb(107, 45, 126);\n"
"border-color: rgb(107, 45, 126);")
        self.next_btn.setObjectName("next_btn")
        self.prev_btn = QtWidgets.QPushButton(self.centralwidget)
        self.prev_btn.setGeometry(QtCore.QRect(120, 430, 121, 71))
        self.prev_btn.setStyleSheet("font: 14pt \"나눔스퀘어\";\n"
"color: rgb(107, 45, 126);\n"
"border-color: rgb(107, 45, 126);")
        self.prev_btn.setObjectName("prev_btn")
        self.result1 = QtWidgets.QLabel(self.centralwidget)
        self.result1.setGeometry(QtCore.QRect(50, 600, 270, 270))
        self.result1.setMinimumSize(QtCore.QSize(270, 270))
        self.result1.setMaximumSize(QtCore.QSize(270, 270))
        self.result1.setText("")
        self.result1.setObjectName("result1")
        self.result2 = QtWidgets.QLabel(self.centralwidget)
        self.result2.setGeometry(QtCore.QRect(360, 600, 270, 270))
        self.result2.setMinimumSize(QtCore.QSize(270, 270))
        self.result2.setMaximumSize(QtCore.QSize(270, 270))
        self.result2.setText("")
        self.result2.setObjectName("result2")
        self.result3 = QtWidgets.QLabel(self.centralwidget)
        self.result3.setGeometry(QtCore.QRect(690, 600, 270, 270))
        self.result3.setMinimumSize(QtCore.QSize(270, 270))
        self.result3.setMaximumSize(QtCore.QSize(270, 270))
        self.result3.setText("")
        self.result3.setObjectName("result3")
        HistoryWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(HistoryWin)
        QtCore.QMetaObject.connectSlotsByName(HistoryWin)

    def retranslateUi(self, HistoryWin):
        _translate = QtCore.QCoreApplication.translate
        HistoryWin.setWindowTitle(_translate("HistoryWin", "MainWindow"))
        self.next_btn.setText(_translate("HistoryWin", "Next"))
        self.prev_btn.setText(_translate("HistoryWin", "Previous"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HistoryWin = QtWidgets.QMainWindow()
    ui = Ui_HistoryWin()
    ui.setupUi(HistoryWin)
    HistoryWin.show()
    sys.exit(app.exec_())

