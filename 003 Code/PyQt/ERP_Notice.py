import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from datetime import datetime
import pymysql
import re

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_Main = uic.loadUiType("C:\PyQt\ERP_Notice.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class NoticeClass(QMainWindow, form_Main) :
    def __init__(self, userID, coopID) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
        
        self.userID = userID
        self.coopID = coopID
        
        column_headers = ['Writer', 'Content','Date Created'] # 테이블위젯 헤더
        
        stylesheet = "::section{background-color:#ffffff}"
        self.noticetable.horizontalHeader().setStyleSheet(stylesheet)
        self.noticetable.verticalHeader().setStyleSheet(stylesheet)
        self.noticetable.setRowCount(50)
        self.noticetable.setColumnCount(3)
        self.noticetable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.noticetable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.noticetable.setHorizontalHeaderLabels(column_headers)
        
        self.btn_main.clicked.connect(self.btn_main_clicked)
        self.btn_borad.clicked.connect(self.btn_borad_clicked)

    
    def btn_main_clicked(self):
        from ERP_Main import MainClass
        self.close()
        self.Main = MainClass(self.userID, self.coopID)
        self.Main.show()
        
    def btn_borad_clicked(self):
        from ERP_Borad import BoradClass
        self.close()
        self.Borad = BoradClass(self.userID, self.coopID)
        self.Borad.show()
        
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myNotice = NoticeClass()

    #프로그램 화면을 보여주는 코드
    myNotice.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    