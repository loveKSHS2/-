# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result_Win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResultsWin(object):
    def setupUi(self, ResultsWin):
        ResultsWin.setObjectName("ResultsWin")
        ResultsWin.resize(1024, 1024)
        ResultsWin.setMinimumSize(QtCore.QSize(1024, 1024))
        ResultsWin.setMaximumSize(QtCore.QSize(1024, 1024))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../.designer/logo_only.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ResultsWin.setWindowIcon(icon)
        ResultsWin.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(ResultsWin)
        self.centralwidget.setObjectName("centralwidget")
        self.picsre_lbl = QtWidgets.QLabel(self.centralwidget)
        self.picsre_lbl.setGeometry(QtCore.QRect(200, 210, 600, 350))
        self.picsre_lbl.setMinimumSize(QtCore.QSize(600, 350))
        self.picsre_lbl.setMaximumSize(QtCore.QSize(600, 350))
        self.picsre_lbl.setStyleSheet("")
        self.picsre_lbl.setText("")
        self.picsre_lbl.setObjectName("picsre_lbl")
        self.results1_lbl = QtWidgets.QLabel(self.centralwidget)
        self.results1_lbl.setGeometry(QtCore.QRect(60, 600, 270, 270))
        self.results1_lbl.setMinimumSize(QtCore.QSize(270, 270))
        self.results1_lbl.setMaximumSize(QtCore.QSize(270, 270))
        self.results1_lbl.setText("")
        self.results1_lbl.setObjectName("results1_lbl")
        self.results2_lbl = QtWidgets.QLabel(self.centralwidget)
        self.results2_lbl.setGeometry(QtCore.QRect(380, 600, 270, 270))
        self.results2_lbl.setMinimumSize(QtCore.QSize(270, 270))
        self.results2_lbl.setMaximumSize(QtCore.QSize(270, 270))
        self.results2_lbl.setText("")
        self.results2_lbl.setObjectName("results2_lbl")
        self.results3_lbl = QtWidgets.QLabel(self.centralwidget)
        self.results3_lbl.setGeometry(QtCore.QRect(700, 600, 270, 270))
        self.results3_lbl.setMinimumSize(QtCore.QSize(270, 270))
        self.results3_lbl.setMaximumSize(QtCore.QSize(270, 270))
        self.results3_lbl.setText("")
        self.results3_lbl.setObjectName("results3_lbl")
        self.mapsbtn = QtWidgets.QPushButton(self.centralwidget)
        self.mapsbtn.setGeometry(QtCore.QRect(830, 480, 93, 91))
        self.mapsbtn.setText("")
        self.mapsbtn.setObjectName("mapsbtn")
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 1024, 1024))
        self.bgLabel.setMinimumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setMaximumSize(QtCore.QSize(1024, 1024))
        self.bgLabel.setText("")
        self.bgLabel.setObjectName("bgLabel")
        self.bgLabel.raise_()
        self.picsre_lbl.raise_()
        self.results1_lbl.raise_()
        self.results2_lbl.raise_()
        self.results3_lbl.raise_()
        self.mapsbtn.raise_()
        ResultsWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(ResultsWin)
        QtCore.QMetaObject.connectSlotsByName(ResultsWin)

    def retranslateUi(self, ResultsWin):
        _translate = QtCore.QCoreApplication.translate
        ResultsWin.setWindowTitle(_translate("ResultsWin", "RESULT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultsWin = QtWidgets.QMainWindow()
    ui = Ui_ResultsWin()
    ui.setupUi(ResultsWin)
    ResultsWin.show()
    sys.exit(app.exec_())

