# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rec_detail.ui'
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
        self.bImg = QtWidgets.QLabel(self.centralwidget)
        self.bImg.setGeometry(QtCore.QRect(140, 250, 350, 270))
        self.bImg.setMinimumSize(QtCore.QSize(350, 270))
        self.bImg.setMaximumSize(QtCore.QSize(350, 270))
        self.bImg.setStyleSheet("")
        self.bImg.setText("")
        self.bImg.setObjectName("bImg")
        self.aImg = QtWidgets.QLabel(self.centralwidget)
        self.aImg.setGeometry(QtCore.QRect(550, 250, 350, 270))
        self.aImg.setMinimumSize(QtCore.QSize(350, 270))
        self.aImg.setMaximumSize(QtCore.QSize(350, 270))
        self.aImg.setText("")
        self.aImg.setObjectName("aImg")
        self.webEV = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEV.setGeometry(QtCore.QRect(140, 610, 771, 351))
        self.webEV.setUrl(QtCore.QUrl("about:blank"))
        self.webEV.setObjectName("webEV")
        self.bText = QtWidgets.QLabel(self.centralwidget)
        self.bText.setGeometry(QtCore.QRect(150, 540, 350, 40))
        self.bText.setMinimumSize(QtCore.QSize(350, 40))
        self.bText.setMaximumSize(QtCore.QSize(350, 40))
        self.bText.setStyleSheet("color: rgb(48, 12, 59);\n"
"font: 20pt \"나눔스퀘어\";")
        self.bText.setText("")
        self.bText.setAlignment(QtCore.Qt.AlignCenter)
        self.bText.setObjectName("bText")
        self.aText = QtWidgets.QLabel(self.centralwidget)
        self.aText.setGeometry(QtCore.QRect(560, 540, 350, 40))
        self.aText.setMinimumSize(QtCore.QSize(350, 40))
        self.aText.setMaximumSize(QtCore.QSize(350, 40))
        self.aText.setStyleSheet("color: rgb(48, 12, 59);\n"
"font: 20pt \"나눔스퀘어\";")
        self.aText.setText("")
        self.aText.setAlignment(QtCore.Qt.AlignCenter)
        self.aText.setObjectName("aText")
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 1024, 1024))
        self.bgLabel.setMinimumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setMaximumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setText("")
        self.bgLabel.setObjectName("bgLabel")
        self.bgLabel.raise_()
        self.bImg.raise_()
        self.aImg.raise_()
        self.webEV.raise_()
        self.bText.raise_()
        self.aText.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recommand Plcae"))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

