import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from datetime import datetime
import pymysql
import re

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_Main = uic.loadUiType("C:\PyQt\ERP_Borad_detalis.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class DetalisClass(QMainWindow, form_Main) :
    def __init__(self, userID, coopID, data, post_id) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
    
        self.userID = userID
        self.coopID = coopID
        self.data = data
        self.post_id = post_id
    
        self.text_show_label.setText(self.data.text())
        
        column_headers = ['Writer', 'Content','Date Created'] # 테이블위젯 헤더
        
        stylesheet = "::section{background-color:#ffffff}"
        self.comments_Widget.horizontalHeader().setStyleSheet(stylesheet)
        self.comments_Widget.verticalHeader().setStyleSheet(stylesheet)
        self.comments_Widget.setRowCount(50)
        self.comments_Widget.setColumnCount(3)
        self.comments_Widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.comments_Widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.comments_Widget.setHorizontalHeaderLabels(column_headers)
        
        com_tabel_add(self)
        
        self.btn_borad.clicked.connect(self.btn_borad_clicked)
        self.btn_com_writing.clicked.connect(self.btn_com_writing_clicked)
        
        con = pymysql.connect(
            host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
            user = 'young',
            password = 'qwer1234',
            database ='erp',
            charset='utf8'
        )
        cur = con.cursor()
        
        cur.execute("SELECT text FROM Commu")

    def btn_borad_clicked(self):
        from ERP_Borad import BoradClass
        self.close()
        self.Borad = BoradClass(self.userID, self.coopID)
        self.Borad.show()
        
    def btn_com_writing_clicked(self):
        comments = self.comments_in_Edit.text()

        con = pymysql.connect(
            host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
            user = 'young',
            password = 'qwer1234',
            database ='erp',
            charset='utf8'
        )
        cur = con.cursor()
        
        now = datetime.now()
        self.today = now.date()
        self.Date_Created = self.today.strftime("%Y-%m-%d")
        
        cur.execute("SELECT STRAIGHT_JOIN cm.Member_name FROM coopMember cm left join coop c on cm.Coop_id = c.Coop_id  WHERE cm.Member_id = %s", (self.userID,))
        userName_cm = cur.fetchall()
        userName = re.sub("[(''),,]","", str(userName_cm))
        
        cur.execute("INSERT INTO Comment(post_id, author, comment, post_date) VALUES (%s, %s, %s, %s)", (self.post_id, userName, comments, self.Date_Created,))
        
        if cur.execute("SELECT author, comment, post_date FROM Comment WHERE post_id = %s", (self.post_id)):
            tablerow = 0
            result = cur.fetchall()
            for row in result:
                self.comments_Widget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
                self.comments_Widget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                self.comments_Widget.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
                tablerow += 1
        
        QMessageBox.about(self, "message", "Created")
        
        con.commit()
        con.close()

def com_tabel_add(self):
    con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
    )
    cur = con.cursor()

    if cur.execute("SELECT author, comment, post_date FROM Comment WHERE post_id = %s", (self.post_id)):
        tablerow = 0
        result = cur.fetchall()
        for row in result:
            self.comments_Widget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.comments_Widget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.comments_Widget.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            tablerow += 1
            
    con.commit()
    con.close()
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myDetalis = DetalisClass()

    #프로그램 화면을 보여주는 코드
    myDetalis.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    