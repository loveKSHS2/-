# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search_Win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchWin(object):
    def setupUi(self, SearchWin):
        SearchWin.setObjectName("SearchWin")
        SearchWin.resize(1024, 1024)
        SearchWin.setMinimumSize(QtCore.QSize(1024, 1024))
        SearchWin.setMaximumSize(QtCore.QSize(1024, 1024))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/logo_only.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchWin.setWindowIcon(icon)
        SearchWin.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SearchWin)
        self.centralwidget.setObjectName("centralwidget")
        self.pics_lbl = QtWidgets.QLabel(self.centralwidget)
        self.pics_lbl.setGeometry(QtCore.QRect(190, 310, 650, 350))
        self.pics_lbl.setMinimumSize(QtCore.QSize(650, 350))
        self.pics_lbl.setMaximumSize(QtCore.QSize(650, 350))
        self.pics_lbl.setStyleSheet("")
        self.pics_lbl.setText("")
        self.pics_lbl.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.pics_lbl.setObjectName("pics_lbl")
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setGeometry(QtCore.QRect(380, 760, 151, 51))
        self.open_btn.setStyleSheet("background-color: rgb(144, 85, 162);\n"
"font: 63 20pt \"NanumSquare\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.open_btn.setObjectName("open_btn")
        self.results_btn = QtWidgets.QPushButton(self.centralwidget)
        self.results_btn.setGeometry(QtCore.QRect(640, 760, 151, 51))
        self.results_btn.setStyleSheet("background-color: rgb(144, 85, 162);\n"
"font: 63 20pt \"NanumSquare\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.results_btn.setObjectName("results_btn")
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 1024, 1024))
        self.bgLabel.setMinimumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setMaximumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bgLabel.setStyleSheet("")
        self.bgLabel.setText("")
        self.bgLabel.setObjectName("bgLabel")
        self.region = QtWidgets.QComboBox(self.centralwidget)
        self.region.setGeometry(QtCore.QRect(130, 760, 151, 51))
        font = QtGui.QFont()
        font.setFamily("210 Namoogulrim")
        font.setPointSize(14)
        self.region.setFont(font)
        self.region.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.region.setObjectName("region")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.region.addItem("")
        self.bgLabel.raise_()
        self.pics_lbl.raise_()
        self.open_btn.raise_()
        self.results_btn.raise_()
        self.region.raise_()
        SearchWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWin)
        QtCore.QMetaObject.connectSlotsByName(SearchWin)

    def retranslateUi(self, SearchWin):
        _translate = QtCore.QCoreApplication.translate
        SearchWin.setWindowTitle(_translate("SearchWin", "EXPLORATION"))
        self.open_btn.setText(_translate("SearchWin", "OPEN"))
        self.results_btn.setText(_translate("SearchWin", "RESULT"))
        self.region.setItemText(0, _translate("SearchWin", "전국"))
        self.region.setItemText(1, _translate("SearchWin", "서울"))
        self.region.setItemText(2, _translate("SearchWin", "경기"))
        self.region.setItemText(3, _translate("SearchWin", "강원"))
        self.region.setItemText(4, _translate("SearchWin", "대전"))
        self.region.setItemText(5, _translate("SearchWin", "인천"))
        self.region.setItemText(6, _translate("SearchWin", "광주"))
        self.region.setItemText(7, _translate("SearchWin", "충북"))
        self.region.setItemText(8, _translate("SearchWin", "충남"))
        self.region.setItemText(9, _translate("SearchWin", "전북"))
        self.region.setItemText(10, _translate("SearchWin", "전남"))
        self.region.setItemText(11, _translate("SearchWin", "경북"))
        self.region.setItemText(12, _translate("SearchWin", "경남"))
        self.region.setItemText(13, _translate("SearchWin", "부산"))
        self.region.setItemText(14, _translate("SearchWin", "대구"))
        self.region.setItemText(15, _translate("SearchWin", "울산"))
        self.region.setItemText(16, _translate("SearchWin", "제주"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWin = QtWidgets.QMainWindow()
    ui = Ui_SearchWin()
    ui.setupUi(SearchWin)
    SearchWin.show()
    sys.exit(app.exec_())

