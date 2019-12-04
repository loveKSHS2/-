import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5 import QtWebEngineWidgets
import sys
import os

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        # QWebEngineView 를 이용하여 웹 페이지를 표출
        web = QWebEngineView()

        ########result.html로 바꿀껏!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        web.load(QUrl().fromLocalFile(
            os.path.split(os.path.abspath(__file__))[0]+r'\result.html'
        ))

        self.form_layout.addWidget(web)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())