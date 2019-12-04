import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from UI import Result_Win
import main2
import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster
from folium import IFrame
import base64
from html_view import Form
import pymysql

class MyResultWin(QMainWindow,Result_Win.Ui_ResultsWin):
    def __init__(self,paths,uid,region):
        super().__init__()
        self.setupUi(self)
        self.id=uid
        self.select_region=region
        self.bgLabel.setStyleSheet('image:url(./views_img/ser_detail_bg.png);')
        self.img_paths=paths
        self.picsre_lbl.setText(self.img_paths)
        self.resultsPics()
        self.html=Form()
        self.rec_btn()

        self.mapsbtn.clicked.connect(self.htmlMap)

    def rec_btn(self):
        self.mapsbtn.setStyleSheet('image:url(./views_img/micon.png); border:0px;')

    def insertsql(self):
        conn = pymysql.connect(host='localhost', user='root', password='love6220',
                               db='userinfo', charset='utf8')
        curs = conn.cursor()
        sql = "INSERT INTO userpaths(u_id, target_path, results_path1, results_path2, results_path3) VALUES(%s, %s, %s, %s, %s)"
        val=(self.id, self.img_paths, self.path[0], self.path[1], self.path[2])
        data = curs.execute(sql, val)
        conn.commit()

    def resultsPics(self):
        self.file = main2.get_cmpr_img_lst(self.select_region)
        self.path = main2.results(self.img_paths,self.file)
        self.insertsql()
        self.gps=main2.get_gps_lst(self.path)
        self.pixmap = QPixmap(self.img_paths)
        self.pixmap = self.pixmap.scaled(600, 350)
        self.picsre_lbl.setPixmap(QPixmap(self.pixmap))
        self.pix1=QPixmap(self.path[0])
        self.pix1 = self.pix1.scaled(270, 270)
        self.pix2=QPixmap(self.path[1])
        self.pix2 = self.pix2.scaled(270, 270)
        self.pix3=QPixmap(self.path[2])
        self.pix3 = self.pix3.scaled(270, 270)
        self.results1_lbl.setPixmap(QPixmap(self.pix1))
        self.results2_lbl.setPixmap(QPixmap(self.pix2))
        self.results3_lbl.setPixmap(QPixmap(self.pix3))
        self.maps()

    def htmlMap(self):

        self.html.show()
    def maps(self):
        m = folium.Map(location=[37.550475, 126.989745], zoom_start=3)
        tooltip = "Click to see picture"
        html = '<img src="data:image/png;base64,{}">'.format
        i = 0
        for ii, kk in self.gps:
            picture = base64.b64encode(open(self.path[i], 'rb').read()).decode()
            iframe = IFrame(html(picture), width=1300 + 20, height=420 + 20)
            popup = folium.Popup(iframe, max_width=650)
            icon = folium.Icon(color="blue")
            folium.Marker(location=[round(float(ii),6),round(float(kk),6)], popup=popup, tooltip=tooltip, icon=icon).add_to(m)
            i += 1
        m.save("result.html")



if __name__=="__main__":
    app=QApplication(sys.argv)
    dig=MyResultWin()
    dig.show()
    sys.exit(app.exec_())
