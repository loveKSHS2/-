import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI import rec_detail

import numpy as np
import folium
from folium.plugins import MarkerCluster
from folium import IFrame
import base64

class RecDetailWin(QMainWindow,rec_detail.Ui_MainWindow):
    def __init__(self, val):
        super().__init__()
        self.setupUi(self)
        self.num = val
        print("selfnum; ",self.num)

        self.bgLabel.setStyleSheet('image:url(./views_img/rec_detail_bg.png);')
        self.pickedImg()
        print("chk")
        self.openWeb()


    def pickedImg(self):
        self.inNameDic = {1:'프랑스 듄느 듀 삘라',2:'태국 우돈타니',3:'일본 메구로 강',4:'미국 바하마 브리겐타인 비치'}
        self.outNameDic = {1:'태안 신두리 해안사구',2:'양평 세미원',3:'진해 여좌천',4:'제주 협재해수욕장'}

        inStr = "image:url(./views_img/rec_img_" + str(self.num) + "_b);"
        outStr = "image:url(./views_img/rec_img_" + str(self.num) + "_a);"

        self.bImg.setStyleSheet(inStr)
        self.aImg.setStyleSheet(outStr)

        self.bText.setText(self.inNameDic[self.num])
        self.aText.setText(self.outNameDic[self.num])

    def openWeb(self):
        gpsTuple = [
            "https://goo.gl/maps/4dZAUrJHCa7hVdzH8",
            "https://goo.gl/maps/LBVePFYnjVHCEVLH7",
            "https://goo.gl/maps/qAJBpcG1AD4aFEQP8",
            "https://goo.gl/maps/dW4tWoH7BGiLqEjF6"
        ]
        #print(type("https://google.com/maps/LBVePFYnjVHCEVLH7"))
        self.webEV.load(QUrl(gpsTuple[self.num-1]))
        #self.webEV.load(QtCore.QUrl(gpsTuple[self.num-1]))
        #self.webEV.setUrl()
        #self.webEV.set
        #self.webEV.load(QtCore.QUrl(gpsTuple[self.num-1]))

'''
    def makeHtml(self):
        
        print(gpsTuple)
        m = folium.Map(location=[37.550475, 126.989745], zoom_start=3)
        html = '<img src="data:image/png;base64,{}">'.format


        icon = folium.Icon(color="blue")
        tooltip = self.inNameDic[self.num]

        loc = list(gpsTuple[self.num-1][0])
        print('loc: ',loc)
        marker = folium.Marker(location=loc, tooltip=tooltip, icon=icon).add_to(m)

        tooltip = self.outNameDic[self.num]
        loc = list(gpsTuple[self.num-1][1])
        print('loc: ', loc)
        marker = folium.Marker(location=loc, tooltip=tooltip, icon=icon).add_to(m)
        m.save("detail.html")
        
'''

if __name__=="__main__":
    print("main")
    app = QApplication(sys.argv)
    m_w = RecDetailWin()
    m_w.show()
    sys.exit(app.exec_())